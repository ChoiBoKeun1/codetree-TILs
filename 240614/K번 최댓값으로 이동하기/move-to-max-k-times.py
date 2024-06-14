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
r,c = map(int,input().split())
r,c = r-1,c-1

cur_num = arr[r][c]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False

    if arr[x][y] >= cur_num:
        return False

    return True

def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def push(x,y):
    visited[x][y] = True
    q.append((x,y))

def bfs():
    global r,c, cur_num

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]


    new_num = 0
    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx,ny):
                push(nx,ny)
                if new_num < arr[nx][ny]:
                    new_num = arr[nx][ny]
                    r,c = nx,ny
                
                if new_num == arr[nx][ny]:
                    if r > nx:
                        r,c = nx,ny
                    elif r == nx and c > ny:
                        r,c = nx,ny

    if new_num == 0:
        return    
    cur_num = new_num

# main
for _ in range(k):
    push(r,c)
    bfs()
    clear_visited()

print(r+1,c+1)