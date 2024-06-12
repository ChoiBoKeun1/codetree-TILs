from collections import deque

q = deque()

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
step = [
    [-1 for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 0:
        return False
    
    return True

def push(x,y, num):
    step[x][y] = num
    q.append((x,y))

def bfs():
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy
            
            if can_go(nx,ny):
                visited[nx][ny] = True
                push(nx,ny, step[x][y]+1)

push(0,0,0)

bfs()
print(step[n-1][m-1])