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

stones = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if arr[i][j]
]
selected_stones = []

def backtrack(cur_num, cnt):
    global ans

    if cnt > m:
        return
    
    if cur_num == len(stones):
        if cnt == m:
            ans = max(ans, calc())
        return

    selected_stones.append(stones[cur_num])
    backtrack(cur_num+1, cnt+1)
    selected_stones.pop()

    backtrack(cur_num+1, cnt)

# ------------------------------
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
    for selected_stone in selected_stones:
        x,y = selected_stone
        arr[x][y] = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    bfs()

    for selected_stone in selected_stones:
        x,y = selected_stone
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    return cnt
# -------------------------

# main
for _ in range(k):
    r,c = map(int, input().split())
    r,c = r-1,c-1
    
    visited[r][c] = True
    q.append((r,c))

    backtrack(0,0)
    
print(ans)