# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:29:02 2015

@author: mcollins
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#on command line:
#%matplotlib qt

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)        # x-array
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

#Init only required for blitting to give a clean slate.
#def init():
#    line.set_ydata(np.ma.array(x, mask=True))
#    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), #init_func=init,
    interval=25, blit=False)
plt.show()