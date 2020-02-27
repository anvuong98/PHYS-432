#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:30:40 2020

@author: vuongthaian
"""

import matplotlib.pyplot as pl
import numpy as np


#pl.ion()
#fig = pl.figure()
#x1, = pl.plot(x, f, 'ro')
#pl.xlim([0, 2*Ngrid])
#pl.ylim([-0.1,1.0])




### Set up the grid
delt = 1 # Temporal increment
delx = 1 # Spatial increment
numGrid = 50; # Grid size
stepMax = 500; # Total number of steps

grid = np.arange(numGrid)*delx # The grid

### Avection speed
u = -0.1 # speed
alpha = u*delt/(2*delx) # Alpha


### The values (and normalization)
f1 = np.copy(grid)*1./numGrid # For FTCS
f2 = np.copy(grid)*1./numGrid # For LF



### Set up plot
pl.ion()
fig, axes = pl.subplots(1,2)
axes[0].set_title('FTCS')
axes[1].set_title('Lax-Friedrichs')


### Plotting intitial state
plt1, = axes[0].plot(grid, f1, 'ro')
plt2, = axes[1].plot(grid, f2, 'ro')
plt1_0 = axes[0].plot(grid, f1)
plt2_0 = axes[1].plot(grid, f2)

for ax in axes:
    ax.set_xlim(0, numGrid)
    ax.set_ylim([0,2])


fig.canvas.draw()

count = 0

while count < stepMax:
    ### The FTCS
    f1[1 : numGrid-1] = f1[1:numGrid-1] - alpha*(f1[2:] - f1[:numGrid-2])
    
    ### The LF method
    f2[1 : numGrid-1] = (1/2) * (f2[2:] + f2[:numGrid-2]) - alpha * (f2[2:] - f2[:numGrid-2])
    
    
    plt1.set_ydata(f1)
    plt2.set_ydata(f2)
    
    fig.canvas.draw()
    pl.pause(0.00001)
    count = count+1
    


    
    
    

