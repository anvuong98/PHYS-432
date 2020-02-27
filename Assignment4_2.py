#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 14:21:08 2020

@author: vuongthaian
"""

import matplotlib.pyplot as pl
import numpy as np



### Set up the grid
delt = 1 # Temporal increment
delx = 1 # Spatial increment
numGrid = 50; # Grid size
stepMax = 500; # Total number of steps

grid = np.arange(numGrid)*delx # The grid

### Parameter
u = -0.1 # speed
alpha = u*delt/(2*delx) # Alpha
D = np.array([0.1,1]) # Diffusion Coefficients
beta = D* delt / (delx)**2 # Beta


### Set up the matrix
A1 = np.eye(numGrid)*(1+2*beta[0]) + np.eye(numGrid, k = 1)*(-beta[0]) + np.eye(numGrid, k=-1) * (-beta[0])  
A1[0][0] = 1 ## Boundary conditions
A1[0][1] = 0 ## Boundary conditions
A1[-1][-1] = 1 ## Boundary conditions
A1[-1][-2] = 0 ## Boundary conditions

    
A2 = np.eye(numGrid)*(1+2*beta[1]) + np.eye(numGrid, k = 1)*(-beta[1]) + np.eye(numGrid, k=-1) * (-beta[1])
A2[0][0] = 1 ## Boundary conditions
A2[0][1] = 0 ## Boundary conditions
A2[-1][-1] = 1 ## Boundary conditions
A2[-1][-2] = 0 ## Boundary conditions


### The values (and normalization)
f1 = np.copy(grid)*1./numGrid # For D[1]
f2 = np.copy(grid)*1./numGrid # For D[2]



### Set up plot
pl.ion()
fig, axes = pl.subplots(1,2)
axes[0].set_title('D = ' +str(D[0]))
axes[1].set_title('D = ' +str(D[1]))


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
    ### The 1st diffusion coefficient
    f1 = np.linalg.solve(A1,f1) # Diffusion term
    f1[1 : numGrid-1] = (1/2) * (f1[2:] + f1[:numGrid-2]) - alpha * (f1[2:] - f1[:numGrid-2]) # LF method
    
    
    ### The 2nd diffusion coefficient
    f2[0: numGrid] = np.linalg.solve(A2,f2) # Diffusion term
    f2[1 : numGrid-1] = (1/2) * (f2[2:] + f2[:numGrid-2]) - alpha * (f2[2:] - f2[:numGrid-2]) # LF method
    
    
    plt1.set_ydata(f1)
    plt2.set_ydata(f2)
    
    fig.canvas.draw()
    pl.pause(0.000001)
    count = count+1