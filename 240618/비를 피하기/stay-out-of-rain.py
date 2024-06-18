from collections import deque

n,h,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

shelters = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if arr[i][j] == 3
]

q = deque()
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

    if arr[x][y] == 1 or visited[x][y]:
        return False

    return True

def push(x,y, new_step):
    q.append((x,y))
    visited[x][y] = True
    step[x][y] = new_step

def bfs():
    while q:
        x,y = q.popleft()

        dxs, dys = [1,0,-1,0], [0,1,0,-1]

        for dx,dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy

            if can_go(nx,ny):
                push(nx, ny, step[x][y] +1)

# main
# 비를 피할수 있는 모든 shelter들을 시작점으로 하는
# bfs 진행

# shelter를 기준으로 진행했기 때문에
# 한번의 bfs로 충분하다.
for x,y in shelters:
    push(x,y,0)

bfs()

for i in range(n):
    for j in range(n):
        if arr[i][j] != 2:
            print(0, end=' ')
        else:
            if not visited[i][j]:
                print(-1, end=' ')
            else:
                print(step[i][j],end=' ')
    print()