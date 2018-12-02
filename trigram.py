'''
Trigram word model from Zhao, Li, Kohonen (2010)
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




