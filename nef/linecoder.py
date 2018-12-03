#!/usr/bin/env python3
'''
Uses a single neuron and a single value to illustrate NEF Principle 1: 
A population of neurons collectively represents a time-varying vector of real
numbers through non-linear encoding and linear decoding.

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
from tuningcurves import curve

if __name__ == '__main__':

    n_samples = 100
    x = np.linspace(.1,1, n_samples)

    alpha = 50
    e = +1
    b = 0
    
    # Plot the theoretical tuning curve
    a = curve(alpha, e, x, b)
    #plt.plot(x, a)
    #plt.xlabel('x')
    #plt.ylabel('Firing rate a (Hz)')
    #plt.show()    

    # Randomly sample values in the interval [-1,+1]
    xsamp = np.random.uniform(.01, 1, n_samples)

    # Compute neuron's activation in response to these samples
    asamp = curve(alpha, e, xsamp, b)

    # Show the samples
    #plt.scatter(xsamp, asamp, s=1.0)
    #plt.xlabel('x')
    #plt.ylabel('Firing rate a (Hz)')
    #plt.show()

    # Swap axes
    plt.scatter(asamp, xsamp, s=1.0)
    plt.xlim([0,40])
    plt.ylim([0,1.1])
    plt.xlabel('Firing rate a (Hz)')
    plt.ylabel('x')
    plt.show()

    # Solve for decoder weight d, discarding everying but slope and intercept
    A = np.vstack([a, np.ones(len(x))]).T
    d = .05 #np.linalg.lstsq(A, x)[0][0]

    # Draw the linear fit
    plt.scatter(asamp, xsamp, s=1.0)
    plt.xlabel('Firing rate a (Hz)')
    plt.ylabel('x')
    t = np.linspace(0,40,n_samples)
    xhat = d * t
    plt.plot(xhat, 'g')
    plt.xlim([0,40])
    plt.ylim([0,1.1])
    plt.title('d = %f' % d)
    plt.show()
