from collections import deque

q = deque()

n,k = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 1:
        return False

    return True

def push(x,y):
    global ans

    ans += 1
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

for _ in range(k):
    r,c = map(int,input().split())
    r,c = r-1, c-1

    if can_go(r,c):
        push(r,c)
    
    bfs()

print(ans)