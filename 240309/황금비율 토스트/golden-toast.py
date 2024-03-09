class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END

    def begin(self):
        return self.head

    def end(self):
        return self.tail

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    def push_back(self, new_data):
        # head와 tail이 같은 경우
        # 1. Node(-1) 인 경우 : 연결리스트가 비어있는 경우
        # 2. Node가 1개 뿐인 경우
        # push_front와 같은 logic을 가진다.
        if self.begin() == self.end():
            self.push_front(new_data)

        else:
            # 구현 편의를 위해 dummy node를 넣어놨기 때문에,
            # 이 연결리스트의 tail은 항상 dummy node임을 잊으면 안된다.
            new_node = Node(new_data)
            new_node.prev = self.tail.prev

            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self, node):
        # node를 삭제하고, node의 next를 return한다.
        next_node = node.next

        # head를 지워야 하는 경우
        if node == self.begin():
            tmp = self.head
            tmp.next.prev = None
            self.head = tmp.next
            tmp.next = None

        # 그외. (원래는 tail 삭제의 경우도 따로 처리가 필요하나,
        # 구현의 간편함을 위해 tail에는 항상 dummy node를 넣어놨기 때문에
        # tail을 삭제할 일은 없다.)
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        return next_node

    # node 앞에 insert 하기.
    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        
        elif node == self.begin():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node

            node.prev.next = new_node
            node.prev = new_node

# 입력
n,m = map(int,input().split())
s = input()

# 연결리스트
l = DoublyLinkedList()
for c in s:
    l.push_back(c)

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
        l.insert(it, cmd[1])

# 출력
it = l.begin()
while it != l.end():
    print(it.data, end='')
    it = it.next