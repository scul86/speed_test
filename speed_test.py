import re
import os
import configparser
import sqlite3 as lite
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd


################################################################################
# Config file stuff
config = configparser.ConfigParser()
config.read(os.path.expanduser('~/Documents/python/speed_test/speed_test.config'))

env_path = os.path.expanduser(config['PATHS'].get('env'))
img_path = os.path.expanduser(config['PATHS'].get('img'))

user = config['PLOTLY'].get('user')
api_key = config['PLOTLY'].get('api_key')
################################################################################

lines = open(os.path.join(env_path, 'speed.txt')).read().splitlines()
p = re.match("Ping: (.*?) ms", lines[0])
d = re.match("Download: (.*?) Mbit/s", lines[1])
u = re.match("Upload: (.*?) Mbit/s", lines[2])
date_time = lines[3]

con = lite.connect(os.path.join(env_path, 'speed.db'))

with con:
    cur = con.cursor()
    cur.execute('''INSERT INTO data(ping,down,up,dt) VALUES(?,?,?,?)''',
                (p.group(1),d.group(1),u.group(1),date_time))

with con:
    cur = con.cursor()
    cur.execute('SELECT id,ping,down,up,dt FROM data')
    rows = cur.fetchall()
df = pd.DataFrame([[ij for ij in i] for i in rows])
df.rename(columns={0: 'id', 1: 'Ping', 2: 'Download', 3: 'Upload', 4:'Date'}, inplace=True);
df = df.sort_values(by=['Date'], ascending=[1])

trace1 = go.Scatter(
     x=df['Date'],
     y=df['Download'],
     name='Download',
)
trace2 = go.Scatter(
    x=df['Date'],
    y=df['Upload'],
    name='Upload',
    yaxis='y2'
)
layout = go.Layout(
    title="Plateau Fiber Speed",
    xaxis=go.XAxis(title='Date'),
    yaxis=go.YAxis(
        title='Download speed (mb/s)',
        range=[0,110]
    ),
    yaxis2=go.YAxis(
        title='Upload speed (mb/s)',
        range=[0,110],
        titlefont=go.Font(
            color='rgb(148, 103, 189)'
        ),
        tickfont=go.Font(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)

py.sign_in(user, api_key)
data = go.Data([trace1,trace2])
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Internet Speeds',world_readable=False,auto_open=False)
py.image.save_as(fig, filename=os.path.join(img_path,'internet_speeds.png'))
