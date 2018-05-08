class Stack(object):
    def __init__(self, capacity):
        self.array = [0 for i in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def push(self, x):
        if self.size < capacity:
            self.size += 1
            self.array[self.size - 1] = x
        else:
            raise ValueError("StackOverflow")

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.array[self.size]
        else:
            raise ValueError("StackUnderflow")

    def peek(self):
        if self.size > 0:
            return self.array[self.size - 1]
        else:
            raise ValueError("StackUnderflow")

capacity = 10
S = Stack(10)
A = list(range(10))
for i in A:
    S.push(i)
B = []
for i in range(len(A)):
    B.append(S.pop())

a = list(reversed(A))
b = B
try:
    assert a == b
except:
    print(a)
    print(b)
