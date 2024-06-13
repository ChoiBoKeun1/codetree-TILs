from collections import deque
q = deque()

n = int(input())
r1,c1, r2,c2 = map(int,input().split())

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False

    return True

def push(x,y,num):
    visited[x][y] = True
    step[x][y] = num
    q.append((x,y))

def bfs():
    dxs = [2,2,-2,-2,1,1,-1,-1]
    dys = [1,-1,1,-1,2,-2,2,-2]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx,ny):
                push(nx,ny, step[x][y]+1)

push(r1,c1,0)