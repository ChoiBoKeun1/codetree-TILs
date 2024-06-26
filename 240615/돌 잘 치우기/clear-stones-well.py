import collections
q = collections.deque()

n,k,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0
start_pos = []
stones = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if arr[i][j]
]
selected_stones = []

# ----------------------------
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and not arr[x][y]

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))

def calc():
    for x,y in selected_stones:
        arr[x][y] = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    for x,y in start_pos:
        visited[x][y] = True
        q.append((x,y))

    bfs()

    for x,y in selected_stones:
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt
# ----------------------------

def backtrack(idx, cnt):
    global ans
    
    if idx == len(stones):
        if cnt == m:
            ans = max(ans, calc())
        return

    selected_stones.append(stones[idx])
    backtrack(idx+1, cnt+1)
    selected_stones.pop()

    backtrack(idx+1, cnt)
# ----------------------------

# main
for _ in range(k):
    r,c = map(int, input().split())
    start_pos.append((r-1,c-1))

backtrack(0,0)
print(ans)