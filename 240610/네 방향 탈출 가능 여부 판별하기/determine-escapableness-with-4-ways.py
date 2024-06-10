from collections import deque
q = deque()

n,m = map(int,input().split())
graph = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or graph[x][y] == 0:
        return False

    return True

def push(x,y):
    visited[x][y] = True
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
                push(nx,ny)
        
push(0,0)
bfs()
print(int(visited[n-1][m-1]))