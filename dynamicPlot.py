# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:41:35 2015

@author: mcollins

#dynamic plot updating (fixed interval)
#plot changes as we change the file
sampleText.txt:
1,4
2,5
3,6
4,3
5,4
6,5
7,7
8,4
9,5
10,3

"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar, yar)
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

import os, time
moddate = os.stat("sampleText.txt")[8] # 10 attributes total
