#!/usr/bin/env python3
'''
vsatest.py : test code for our VSA class in Assignment #7

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

from vsa import VSA

print('\nPart 2 -----------------------------')

vsa = VSA(1000)

a = vsa.randvec('A')
b = vsa.randvec('B')
c = vsa.randvec('C')
d = vsa.randvec('D')
x = a*b + c*d
y = c*x

print('\nWinner is ' + vsa.winner(y) + ' (should be D)')

print('\nPart 3 -----------------------------')

vsa = VSA(10000) # Ten thousand elements, as per Kanerva (2008)
nam = vsa.randvec('name')
usa = vsa.randvec('USA')
cap = vsa.randvec('capital')
wdc = vsa.randvec('Washington, DC')
mon = vsa.randvec('money')
dol = vsa.randvec('dollar')
mex = vsa.randvec('Mexico')
mxc = vsa.randvec('Mexico City')
pes = vsa.randvec('peso')
ustates = nam*usa + cap*wdc + mon*dol
mexico  = nam*mex + cap*mxc + mon*pes
fum = ustates * mexico
query = dol*fum
print('\nWinner is ' + vsa.winner(query) + ' (should be peso)')

print('\nPart 5 -----------------------------')

vsa = VSA(10000)

a = vsa.randvec('A')
b = vsa.randvec('B')
c = vsa.randvec('C')
d = vsa.randvec('D')
e = vsa.randvec('E')
f = vsa.randvec('F')
g = vsa.randvec('G')

x = vsa.seqencode(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
print('\nDecoded sequence is ' + str(vsa.seqdecode(x)) + ' (should be [A, B, C, D, E, F, G])')

x = vsa.seqencode(['A', 'C', 'E'])
print('\nDecoded sequence is ' + str(vsa.seqdecode(x)) + ' (should be [A, C, E])')
