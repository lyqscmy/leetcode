class Queue(object):
    def __init__(self, capacity):
        self.array = [0 for i in range(capacity + 1)]
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def enqueue(self, x):
        if self.size == self.capacity:
            raise ValueError("QueueOverflow")
        self.array[self.tail] = x
        self.size += 1
        if self.tail == self.capacity:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            raise ValueError("QueueUnderflow")
        x = self.array[self.head]
        self.size -= 1
        if self.head == self.capacity:
            self.head = 0
        else:
            self.head += 1
        return x


q = Queue(4)
for i in range(4):
    q.enqueue(i)
try:
    q.enqueue(1)
except ValueError:
    pass

for i in range(4):
    q.dequeue()
try:
    q.dequeue()
except ValueError:
    pass

A = list(range(3))
for i in A:
    q.enqueue(i)

B = []
for i in range(3):
    B.append(q.dequeue())

a = A
b = B

try:
    assert a == b
except:
    print(a)
    print(b)
