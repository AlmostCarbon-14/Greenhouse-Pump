#!/usr/bin/env python3
import RPi.GPIO as gpio
import time
import datetime

channel_1 = 17
channel_2 = 27

gpio.setmode(gpio.BCM)
gpio.setup(channel_1, gpio.OUT)
gpio.setup(channel_2, gpio.OUT)

def pump_on(pin):
    gpio.output(pin, gpio.HIGH)

def pump_off(pin):
    gpio.output(pin, gpio.LOW)

time_1 = 35

time_2 = 35

#setting up cronjob to start at startup

if __name__ == '__main__':
    try:
        pump_on(channel_1)
        datetime = datetime.datetime.now()
        print("...Activating Sprinkler 1...: ", str(datetime))
        time.sleep(time_1) #change to 70
        print("...Deactivating Sprinkler 1...")
        pump_off(channel_1)
        
        pump_on(channel_2)
        print("...Activating Sprinkler 2...: ", str(datetime))
        time.sleep(time_2)
        print("...Deactivating Sprinkler 2...")
        pump_off(channel_2)

        gpio.cleanup()
    except KeyboardInterrupt:
        gpio.cleanup()
        print("Interrupted!")
        pass
    except AttributeError:
        gpio.cleanup()
        print("Error!\n")
        pass
