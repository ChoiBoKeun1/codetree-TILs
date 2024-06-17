import collections
q = collections.deque()

n,k,u,d = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

def print_arr(arr):
    for row in arr:
        for col in row:
            print(col, end=' ')
        print()
    print()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# x,y 위치로 갈수 있는가?
# pre_h : 이전 위치의 높이
def can_go(x,y, pre_h):
    if not in_range(x,y):
        return False
        
    if visited[x][y]:
        return False
    
    dist = abs(pre_h - arr[x][y])

    if u > dist or d < dist:
        return False

    return True

def push(x,y):
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy

            if can_go(nx,ny, arr[x][y]):
                push(nx,ny)

def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

selected = []
tmp_visited = [False] * (n*n)

def convert(num):
    row = num // n
    col = num % n

    return (row,col)

def calc():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    return cnt

ans = 0
def backtrack(cnt):
    global ans
    
    if cnt == k:
        for s in selected:
            r,c = convert(s)
            push(r,c)
        bfs()
        ans = max(ans,calc())
        clear_visited()
        return

    for i in range(n*n):
        if tmp_visited[i]:
            continue

        tmp_visited[i] = True            
        selected.append(i)
        backtrack(cnt +1)
        tmp_visited[i] = False
        selected.pop()

backtrack(0)
print(ans)