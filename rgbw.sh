#!/usr/bin/env bash
# turns on repeated start required by rgbw sensor
sudo sh -c '/bin/echo Y > /sys/module/i2c_bcm2708/parameters/combined'
# turns off repeated start required by rgbw sensor
# sudo sh -c '/bin/echo N > /sys/module/i2c_bcm2708/parameters/combined'
