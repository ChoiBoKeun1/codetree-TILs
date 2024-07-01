n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

cells = list()
ans = 0

def initialize():
    for i in range(n):
        for j in range(n):
            cells.append((arr[i][j], i, j))

    cells.sort()

    for i in range(n):
        for j in range(n):
            dp[i][j] = 1

# main
initialize()

for _, x, y in cells:
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    for dx,dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and arr[nx][ny] > arr[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)