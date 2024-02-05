n,m = map(int,input().split())
arr = [
    [""] * m
    for _ in range(n)
]
# 남서북동
dx,dy = [1,0,-1,0], [0,-1,0,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def next_char(c):
    if c == 'Z':
        return 'A'
    return chr(ord(c) + 1)

x,y = 0,0
arr[0][0] = 'A'
cur_dir = 3

for i in range(2, n*m+1):
    nx, ny = x + dx[cur_dir], y + dy[cur_dir]

    # 방향 전환
    if not in_range(nx,ny) or arr[nx][ny] != "":
        cur_dir = (cur_dir + 1) % 4
        nx, ny = x + dx[cur_dir], y + dy[cur_dir]
    arr[nx][ny] = next_char(arr[x][y])
    x,y = nx,ny
    
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()