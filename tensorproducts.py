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
