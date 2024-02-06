n,t = map(int,input().split())
cmd = input()
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

x,y = n // 2, n // 2
# 동남서북
dx,dy = [0,1,0,-1], [1,0,-1,0]
cur_dir = 3

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

ans = arr[x][y]
for elem in cmd:
    if elem == 'L':
        cur_dir = (cur_dir - 1 + 4) % 4
    elif elem == 'R':
        cur_dir = (cur_dir + 1) % 4
    else:
        nx, ny = x + dx[cur_dir], y + dy[cur_dir]
        if in_range(nx,ny):
            ans += arr[nx][ny]
            x,y = nx,ny

print(ans)