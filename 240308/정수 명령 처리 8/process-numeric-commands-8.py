class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, n):
        new_node = Node(n)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        
        self.node_num += 1

    def push_back(self, n):
        new_node = Node(n)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            return "List is empty"
        
        elif self.head.next == None:
            tmp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return tmp.data

        else:
            tmp = self.head
            tmp.next.prev = None
            self.head = tmp.next
            tmp.next = None

            self.node_num -= 1
            return tmp.data
    
    def pop_back(self):
        if self.tail == None:
            return "List is empty"

        elif self.tail.prev == None:
            tmp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return tmp.data

        else:
            tmp = self.tail
            tmp.prev.next = None
            self.tail = tmp.prev
            tmp.prev = None

            self.node_num -= 1
            return tmp.data
    
    def size(self):
        return self.node_num

    def empty(self):
        return int(self.node_num == 0)
    
    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data


n = int(input())
MyList = DoublyLinkedList()

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        MyList.push_front(cmd[1])
    elif cmd[0] == 'push_back':
        MyList.push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        print(MyList.pop_front())
    elif cmd[0] == 'pop_back':
        print(MyList.pop_back())
    elif cmd[0] == 'size':
        print(MyList.size())
    elif cmd[0] == 'empty':
        print(MyList.empty())
    elif cmd[0] == 'front':
        print(MyList.front())
    elif cmd[0] == 'back':
        print(MyList.back())