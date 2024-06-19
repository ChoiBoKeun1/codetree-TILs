from collections import deque
import sys
q = deque()
INT_MAX = sys.maxsize

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
    [INT_MAX for _ in range(n)]
    for _ in range(n)
]

r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 1:
        return False

    return True

def push(x,y, num):
    step[x][y] = num
    visited[x][y] = True
    q.append((x,y))

def clear_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = x + dx , y + dy

            if can_go(nx,ny):
                push(nx,ny, step[x][y]+1)

walls = [
    (i,j)
    for i in range(n)
    for j in range(n)
    if arr[i][j] == 1
]
selected_walls = []

def calc():
    global r1,c1, r2,c2

    # 선택한 벽들을 arr에서 제거한다.
    for x,y in selected_walls:
        arr[x][y] = 0

    # visited 초기화
    clear_visited()

    # 시작점
    push(r1 -1, c1 -1, 0)

    # bfs 진행
    bfs()

    # 선택한 벽들 arr에 다시 복구
    for x,y in selected_walls:
        arr[x][y] = 1

    return step[r2 -1][c2 -1]

ans = INT_MAX
def backtrack(idx, cnt):
    global ans

    if idx == len(walls):
        if cnt == k:
            ans = min(ans, calc())
        return

    selected_walls.append(walls[idx])
    backtrack(idx +1, cnt +1)
    selected_walls.pop()

    backtrack(idx +1, cnt)

backtrack(0,0)
if ans == INT_MAX:
    ans = -1
print(ans)