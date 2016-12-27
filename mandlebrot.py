# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:19:56 2015

@author: mcollins
"""

#mandlebrot.py
#produce image of variant on mandlebrot set
#all c such that iteration z <- z^2 + z + c is bounded
#when started at z_0 = 0

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

maxIter = 150
gridsize = 2048

#grid of values for c
# could also use builtin np.meshgrid
rgrid = np.linspace(-1.25, -0.75, gridsize) #real part of c
igrid = np.linspace(-0.25, 0.25, gridsize) #imag part of c
c = np.array([[complex(rgrid[i], igrid[j]) for i in range(gridsize)] for j in range(gridsize)])

#matrix of iterates: Z[x,y] = z_n with c = rgrid[x] + i*igrid[y]
Z = np.zeros((gridsize, gridsize))
#color == 0 for points in set, otherwise color indicates speed of divergence
colors = np.zeros((gridsize, gridsize))

DivergenceThresh = 3 
for t in range(maxIter):
    #Z = Z*Z + Z + c
    Z = Z*Z + c 
    #no need to go off to infinity, abs>DivergenceThresh implies divergence
    Z = np.where(np.abs(Z) > DivergenceThresh , DivergenceThresh, Z )
    if t > DivergenceThresh:
        colors = np.where( (colors == 0) & (np.abs(Z) >= DivergenceThresh) , t, colors)

#Display results
#Mset = np.abs(Z) < 2
plt.imshow(colors)


