class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def top(self):
        return self.items[-1]

myStack = Stack()
n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push':
        myStack.push(cmd[1])
    elif cmd[0] == 'pop':
        print(myStack.pop())
    elif cmd[0] == 'size':
        print(myStack.size())
    elif cmd[0] == 'empty':
        print(int(myStack.empty()))
    elif cmd[0] == 'top':
        print(myStack.top())