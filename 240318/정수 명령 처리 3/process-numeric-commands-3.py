from collections import deque

dq = deque()

n = int(input())
for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])

    elif cmd[0] == 'pop_front':
        print(dq.popleft())

    elif cmd[0] == 'pop_back':
        print(dq.pop())

    elif cmd[0] == 'size':
        print(len(dq))

    elif cmd[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
        # print(1 if not dq else 0)

    elif cmd[0] == 'front':
        print(dq[0])

    elif cmd[0] == 'back':
        print(dq[-1])