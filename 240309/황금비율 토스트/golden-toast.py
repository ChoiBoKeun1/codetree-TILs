class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    def push_back(self, new_data):
        if self.begin() == self.end():
            self.push_front(new_data)
        
        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev

            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self, node):
        next_node = node.next

        if node == self.begin():
            tmp = self.head
            tmp.next.prev = None
            self.head = tmp.next
            tmp.next = None
        
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node
    
    def insert(self, node, new_data):
        if node == self.begin():
            self.push_front(new_data)
        
        elif node == self.end():
            self.push_back(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node

            node.prev.next = new_node
            node.prev = new_node

    def begin(self):
        return self.head

    def end(self):
        return self.tail

# 입력
n,m = map(int,input().split())
bread = input()

# 연결리스트
l = DoublyLinkedList()
for elem in bread:
    l.push_back(elem)

# iterator
it = l.end()

for _ in range(m):
    cmd = input().split()

    if cmd[0] == 'L':
        if it != l.begin():
            it = it.prev
    
    elif cmd[0] == 'R':
        if it != l.end():
            it = it.next

    elif cmd[0] == 'D':
        if it != l.end():
            it = l.erase(it)
            
    elif cmd[0] == 'P':
        l.insert(it,cmd[1])

# 출력
it = l.begin()
while it != l.end():
    print(it.data, end='')
    it = it.next