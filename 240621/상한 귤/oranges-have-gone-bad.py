from collections import deque

n,k = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
step = [
    [-2 if arr[i][j] == 1 else -1 for j in range(n)]
    for i in range(n)
]

q = deque()

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and not arr[x][y] == 0

def push(x, y, new_step):
    q.append((x,y))
    visited[x][y] = True
    step[x][y] = new_step

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy
            
            if can_go(nx,ny):
                push(nx,ny, step[x][y] + 1)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            push(i,j,0)
bfs()

print_arr(step)