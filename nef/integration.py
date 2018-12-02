#!/usr/bin/env python3
'''
Leaky integration vs. standard integration

Copyright (C) Simon D. Levy 2018

This file is part of csci252-examples.

csci252-examples is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
'''

import numpy as np
import matplotlib.pyplot as plt

def integrate(x, leak=0):
    n = len(x)
    y = np.zeros(n)
    for k in range(1,n):
        y[k] = y[k-1] + x[k] - leak*y[k-1] 
    return y

N = 50

# Generate a constant signal
x = .3*np.ones(N)

# Plot the signal
plt.subplot(3,1,1)
plt.ylim([0,1.1])
plt.plot(x)

# Plot standard integration
plt.subplot(3,1,2)
plt.plot(integrate(x))

# Plot leaky integration
plt.subplot(3,1,3)
plt.plot(integrate(x,.1))

plt.show()
    

