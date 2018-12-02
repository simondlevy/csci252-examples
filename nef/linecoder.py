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

def plotcurve(alpha, e, x, b, style='b'):

    plt.plot(x, curve(alpha, e, x, b), style)

def finishplot():

    plt.xlim([-1,+1])
    plt.ylim([.1,50])
    plt.xlabel('x')
    plt.ylabel('Firing rate a (Hz)')
    plt.show()    

if __name__ == '__main__':

    n_samples = 100
    x = np.linspace(+1,-1, n_samples)

    alpha = 50
    e = +1
    b = 10
    
    # Plot the theoretical tuning curve
    plotcurve(alpha, e, x, b, 'b')
    finishplot()

    # Randomly sample values in the interval [-1,+1]
    x = np.random.uniform(-1, +1, n_samples)

    # Compute neuron's activation in response to these samples
    a = curve(alpha, e, x, b)

    # Show the samples
    plt.scatter(x, a, s=1.0)
    plt.xlim([-1,+1])
    plt.ylim([0,50])
    plt.xlabel('x')
    plt.ylabel('Firing rate a (Hz)')

    # Solve for decoder weight d, discarding everying but slope and intercept
    X = np.vstack([x, np.ones(len(x))]).T
    d = np.linalg.lstsq(X, a)[0][0]
    print('d = %+2.2f' % d)

    # Draw the linear fit
    plt.plot(x, x*d, 'g')
    plt.show()
