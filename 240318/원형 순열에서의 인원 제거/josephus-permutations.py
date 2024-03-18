from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def pop(self):
        return self.dq.popleft()

    def top(self):
        return self.dq[0]

    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def printQ(self):
        print(self.dq)

n,k = map(int,input().split())
myQ = Queue()

for i in range(1, n+1):
    myQ.push(i)

while myQ.empty() == False:
    for i in range(1, k):
        myQ.push(myQ.pop())
    
    print(myQ.pop(), end=' ')