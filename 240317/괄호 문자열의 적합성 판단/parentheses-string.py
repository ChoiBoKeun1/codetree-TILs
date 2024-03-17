class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def empty(self):
        return not self.items

    def pop(self):
        if not self.empty():
            return self.items.pop()
    
    def top(self):
        if not self.empty():
            return self.items[-1]

import sys

s = input()
myStack = Stack()

for i in range(len(s)):
    if s[i] == '(':
        myStack.push(s[i])
    else:
        if myStack.empty():
            print("No")
            sys.exit()
        else:
            myStack.pop()

print("Yes")