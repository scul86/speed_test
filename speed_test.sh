#!/usr/bin/env bash

/home/$USER/Documents/python/speed_test/venv/bin/python3 /home/$USER/Documents/python/speed_test/venv/lib/python3.5/site-packages/speedtest_cli.py --simple > /home/$USER/Documents/python/speed_test/speed.txt

date -u "+%F %T" >> /home/$USER/Documents/python/speed_test/speed.txt