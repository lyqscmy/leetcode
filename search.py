import bisect
import random


def bsearch(A, x, lo, hi):
    mid = lo + (hi - lo) // 2
    while lo < hi:
        if A[mid] < x:
            lo = mid + 1
        else:
            hi = mid
        mid = lo + (hi - lo) // 2
    if A[mid] == x:
        return mid
    else:
        return -1


A = list(range(100))
x = 55

a = A[bsearch(A, x, 0, len(A) - 1)]
b = x
try:
    assert a == b
except:
    print(a)
    print(b)

A = list(range(100))
x = 101

a = bsearch(A, x, 0, len(A) - 1)
b = -1
try:
    assert a == b
except:
    print(a)
    print(b)

A = list(range(100))
B = [33, 44, 55, 66, 77, 88]
for i in B:
    j = bisect.bisect_left(A, i)
    A.insert(j, i)
x = 66

a = A[bsearch(A, x, 0, len(A) - 1)]
b = x
try:
    assert a == b
except:
    print(a)
    print(b)
