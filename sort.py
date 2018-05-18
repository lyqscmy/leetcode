import random


def bubbleSort1(A):
    n = len(A)
    while True:
        swaped = False
        for i in range(1, n):
            if A[i - 1] > A[i]:
                tmp = A[i]
                A[i] = A[i - 1]
                A[i - 1] = tmp
                swaped = True
        if not swaped:
            break


def bubbleSort2(A):
    n = len(A)
    while n > 0:
        for i in range(1, n):
            if A[i - 1] > A[i]:
                tmp = A[i]
                A[i] = A[i - 1]
                A[i - 1] = tmp
        n -= 1


def insertSort(A):
    size = len(A)
    for i in range(1, size):
        key = A[i]
        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            i -= 1
        A[i] = key


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def topk(A, p, r, k):
    k0 = k - p
    if k0 >= p and k <= r:
        q = partition(A, p, r)
        while q != k0:
            if k < q:
                r = q - 1
            else:
                p = q + 1
            q = partition(A, p, r)
        return A[q]
    else:
        return None


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp

    tmp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = tmp
    return i + 1


xs = list(range(100))
random.shuffle(xs)

k = 4 # 0-based
a = k
b = topk(xs, 0, len(xs) - 1, k)

try:
    assert a == b
except:
    print(a)
    print(b)
