# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 18:12:47 2015

@author: mcollins
"""



import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5), dpi=80)
ax1=fig.add_subplot(2,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

lC = ax1.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label='cos')
ax2 = fig.add_subplot(2,1,2)
lS = ax2.plot(X, S, color="red", linewidth=2.5, linestyle="-", label='sin')

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data',0))
ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data',0))

#these will apply to the current subplot (ax2); or plt.sca(ax1)
plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
plt.legend(loc='upper left')
plt.show()





