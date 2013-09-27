__author__ = 'mc'

import numpy.random as nprnd


def leftchild(i):
    return 2 * i + 1


def rightchild(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) / 2


def max_heapify(A, i):
    l = leftchild(i)
    r = rightchild(i)
    largest = i

    if l <= len(A) - 1 and A[l] > A[i]:
        largest = l

    if r <= len(A) - 1 and A[r] > A[largest]:
        largest = r

    if i != largest:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest)

    return A


def build_max_heap(A):
    for i in range((len(A) - 1) / 2, -1, -1):
        A = max_heapify(A, i)
    return A


def heapsort(A):
    A = build_max_heap(A)
    res = []
    for i in range(0, len(A)):
        temp = A[0]
        A[0] = A[len(A)-1]
        A[len(A)-1] = temp
        res.append(A.pop())
        max_heapify(A, 0)

    return res



v = nprnd.randint(1, 1000, 10).tolist()
print v
#print build_max_heap(v)
print sorted(v, reverse=True)
print heapsort(v)

