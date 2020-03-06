'''
lsa.py : Latent Semantic Analysis on a tiny text corpus

Based on http://www1.se.cuhk.edu.hk/~seem5680/lecture/LSI-Eg.pdf

Simon D. Levy
CSCI 252
24 Oct 2018
'''

import numpy as np

def mag(a):
    return np.sqrt(np.sum(a**2))

def cosine(a, b):
    return np.dot(a,b) / (mag(a) *  mag(b))

# Our three "documents"
d1 = 'Shipment of gold damaged in a fire.'
d2 = 'Delivery of silver arrived in a silver truck.'
d3 = 'Shipment of gold arrived in a truck.'

print('Step 1: Set term weights and construct the term-document matrix A and query matrix\n')

# Turn each document into an unpunctuated list of lower-case terms (words)
d1 = [w.lower() for w in d1.replace('.', ' ').split()]
d2 = [w.lower() for w in d2.replace('.', ' ').split()]
d3 = [w.lower() for w in d3.replace('.', ' ').split()]

# Make a set of all terms, sorted alphabetically
terms = sorted(set(d1 + d2 + d3))

# Build an occurrence matrix A from the set
n = len(terms)
A = np.zeros((n,3))
for k in range(n):
    A[k] = np.array([doc.count(terms[k]) for doc in (d1,d2,d3)])


# Build a query vector
q = np.array([word in ['gold', 'silver', 'truck'] for word in terms]).astype(int)

for term,v,s in zip(terms,A,q):
    print('%10s' % term, v, s)

print('\nStep 2: Decompose matrix A matrix and find the U, S and V matrices,')
print('        where A = USV^T\n')

U,S,V = np.linalg.svd(A, full_matrices=False)

np.set_printoptions(precision=4)
print('U=\n',U)
print('\nS=\n',S)
print('\nV=\n', V)

print('\nStep 3:  Implement a Rank 2 Approximation by keeping the first two columns of')
print('         U and V and the first two columns and rows of S.\n')

U = U[:,:2]
V = V[:2,:]
S = S[:2]

print('\nU=\n', U)
print('\nS=\n', S)
print('\nV=\n', V)

print('\nStep 4: Find the new document vector coordinates in this reduced 2-dimensional')
print('        space.\n')

d1 = V[:,0]
print('d1: ', d1)
d2 = V[:,1]
print('d2: ', d2)
d3 = V[:,2]
print('d3: ', d3)

print('\nStep 5: Find the new query vector coordinates in the reduced 2-dimensional')
print('        space.\n')

q = np.dot(q, np.dot(U, np.linalg.inv(np.diag(S))))
print('q = ', q)

print('\nStep 6: Rank documents in decreasing order of query-document cosine')
print('        similarities.\n')

print('sim(q,d1) = %+3.3f' % cosine(d1, q))
print('sim(q,d2) = %+3.3f' % cosine(d2, q))
print('sim(q,d3) = %+3.3f' % cosine(d3, q))





