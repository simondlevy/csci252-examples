#!/usr/bin/env python3
'''
Simple illustration of tensor products using Gayler's MAP architecture

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

def mag(x):
    return np.sqrt(np.dot(x,x))

def cosine(x, y):
    return np.dot(x,y) / (mag(x)*mag(y))

# Use only -1,+1 values
red      = np.random.randint(0, 2, 1000) * 2 - 1
square   = np.random.randint(0, 2, 1000) * 2 - 1
blue     = np.random.randint(0, 2, 1000) * 2 - 1
triangle = np.random.randint(0, 2, 1000) * 2 - 1

rsbt = np.outer(red, square) + np.outer(blue, triangle)

query = np.diagonal(rsbt / square)

print(cosine(query, red))
print(cosine(query, square))
print(cosine(query, blue))
print(cosine(query, triangle))
