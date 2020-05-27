#!/usr/bin/env python3


import matplotlib.pyplot as plt
import pandas as pd
import os

PATH_OUT = "Graphs/Output.png"

with open('Logs/humid.log') as f:
    data = [line.rstrip() for line in f]

for x in range(0, len(data)):
    data[x] = data[x].split(" ")

tups = []

for line in data:
    tups.append([float(line[1]), float(line[4]), str(line[7][5:] + ' ' + line[8][0:5])])

for tup in tups:
    if tup[1] > 100:
        tup[1] = float('nan')

temp = []
humidity = []
date = []
for tup in tups:
    temp.append(tup[0])
    humidity.append(tup[1])
    date.append(tup[2])

figure, axes = plt.subplots(figsize = (15,8))

axes.plot(date, temp)
plt.xticks(rotation = 45)
axes.plot(humidity)
axes.set_ylabel('Value')
axes.set_xlabel('Datetime')
plt.legend(['Temp F', 'Humidity %'], loc = 'upper left')
if os.path.exists(PATH_OUT):
    os.remove(PATH_OUT)

plt.savefig(PATH_OUT)
