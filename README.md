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
...    id INTEGER primary key autoincrement,
...    ping INTEGER not null,
...    down INTEGER not null,
...    up   INTEGER not null,
...    dt   DATETIME not null
...    );
sqlite> .exit
```

#### Personalize speed_test.config
Change `speed_test.config` to contain your Plotly username and API key

# Run
---
```sh
$ ~/Documents/python/speed_test/speed_test.sh
$ ~/Documents/python/speed_test/speed_test_wrapper.sh
```
This should export a `.png` of the graph at `speed_test/internet_speeds.png`, and send the same data to your Plotly account

# Automation
---
I run this automatically every 30 minutes with crontab:
```sh
$ crontab -e
# m   h  dom mon dow   command
0,30  *  *   *   *    ~/Documents/python/speed_test/speed_test.sh
10,40 *  *   *   *    ~/Documents/python/speed_test/speed_test_wrapper.sh
```
This fetches the speed_test data every hour at 0 and 30 minutes, then, every hour at 10 and 40 minutes, reads, stores it in the db, and pushes to Plotly.

# Improvements
---
I do not like having to use the `speed_test_wrapper.sh`, but the shebang doesn't expand the `$USER` variable, and this was the way I found to get around that LIMFAC.
