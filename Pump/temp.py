#!/usr/bin/python
import sys
import Adafruit_DHT
import time
import datetime
CEL = 9/5

def fahren(temp):
    return (temp * CEL) + 32

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print 'Temp: {0:0.1f} F, Humidity: {1:0.1f} %, at {2}'.format(fahren(temperature), humidity, str(datetime.datetime.now()))

