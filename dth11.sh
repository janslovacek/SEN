#!/usr/bin/env bash
sudo apt-get install build-essential
sudo apt-get install python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
