#!/usr/bin/env python3
'''
Trigram word model from Zhao, Li, Kohonen (2010)

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

NDIMS = 100

def normalize(x):

    return x / np.sum(x)

def main():

    novel = open('mobydick.txt', encoding='utf8').read().split()

    novel = [word.lower() for word in novel]

    words = set(novel)

    d = {}

    for word in words:
        
        d[word] = np.random.random(NDIMS)

    for k in range(1,len(novel)-1):

        word = novel[k]

        left = novel[k-1]

        right = novel[k+1]

        d[word] = normalize(d[left] + d[word] + d[right])

    print(len(d.keys()))

main()




