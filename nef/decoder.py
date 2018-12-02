#!/usr/bin/env python3
'''
Illustrates NEF Principle 1: A population of neurons collectively represents a
time-varying vector of real numbers through non-linear encoding and linear
decoding.
'''

import numpy as np
import matplotlib.pyplot as plt
from tuningcurves import curve

# Parameters to experiment with
N_SAMPLES = 200
RADIUS    = 30
ALPHA     = 100
E         = +1
B         = 0

# Randomly sample values in the interval [0,RADIUS]
x = np.random.uniform(0, RADIUS, N_SAMPLES)

# Compute neuron's activation in response to these samples
a = curve(ALPHA, E, x, B)

# Show the samples
plt.scatter(x, a, s=1.0)
plt.xlabel('x')
plt.ylabel('a')
plt.show()

# Solve for decoder weight d, discarding everying but slope
X = np.vstack([x, np.ones(len(x))]).T
d = np.linalg.lstsq(X, a)[0][0]
print(d)

