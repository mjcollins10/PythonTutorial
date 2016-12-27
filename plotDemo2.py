

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,5), dpi=80)
ax=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

f=plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label='cos')
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label='sin')

#ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.xlim(X.min()*1.1, X.max()*1.1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.ylim(C.min()*1.1,C.max()*1.1)
plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
       
plt.legend(loc='upper left')
plt.show()

#updating plot -- also see 'animation' submodule
#type(f)
#Out[10]: matplotlib.lines.Line2D

f[0].set_ydata(C/3)
plt.draw()
