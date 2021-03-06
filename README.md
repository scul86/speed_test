# speed_test
---
Tests your internet speed, stores in a database, and plots trends on [plotly](https://plot.ly).

# Install
---
Clone the repository:
```sh
$ git clone https://github.com/scul86/speed_test.git
```
Or download [release zip](https://github.com/scul86/speed_test/releases)

#### Configure your python environment
I prefer to use `virtualenv` for my python environment...
```sh
$ virtualenv -p python3 venv
$ venv/bin/pip install -r requirements.txt
```
Note, you might have to install `Cython` as well:
```sh
$ venv/bin/pip install Cython
```

#### Set up the database:
```sh
$ sqlite3 speed.db
sqlite> CREATE TABLE data(
...    id INTEGER PRIMARY KEY AUTOINCREMENT,
...    ping INTEGER NOT NULL,
...    down INTEGER NOT NULL,
...    up   INTEGER NOT NULL,
...    dt   DATETIME DEFAULT CURRENT_TIMESTAMP
...    );
sqlite> .exit
```

#### Personalize speed_test.config
Change `speed_test.config` to contain your desired Paths and Plotly information.

# Run
---
```sh
$ ~/Documents/python/speed_test/speed_test.sh
```
This should export a `.png` of the graph at `[IMG_PATH]/internet_speeds.png`, and send the same data to your Plotly account

# Automation
---
I run this automatically every 30 minutes with crontab:
```sh
$ crontab -e
# m   h  dom mon dow   command
0,30  *  *   *   *    ~/Documents/python/speed_test/speed_test.sh >> ~/Documents/python/speed_test/speed.log 2>&1
```
This fetches the speed_test data every hour at 0 and 30 minutes, then reads, stores it in the db, and pushes to Plotly.

# Improvements
---
Please submit a bug report if you find something that could be improved!
