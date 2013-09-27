import numpy.random as nprnd

v = nprnd.randint(1, 1000, 1000).tolist()

def insertionsort(v):
    for j in range(2, len(v)):
        key = v[j]
        i = j - 1
        while i >= 0 and v[i] > key:
            v[i+1] = v[i]
            i = i - 1
        v[i+1] = key

    return v

print insertionsort(v)