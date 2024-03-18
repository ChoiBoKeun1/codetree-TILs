from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq.popleft()

    def front(self):
        if self.empty():
            raise Exception("Queue is empty")

        return self.dq[0]

n = int(input())
myQ = Queue()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        myQ.push(cmd[1])
    
    elif cmd[0] == 'pop':
        print(myQ.pop())

    elif cmd[0] == 'size':
        print(myQ.size())

    elif cmd[0] == 'empty':
        print(int(myQ.empty()))

    elif cmd[0] == 'front':
        print(myQ.front())