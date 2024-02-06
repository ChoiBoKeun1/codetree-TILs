n = int(input())

arr = [
    [0] * n
    for _ in range(n)    
]

x,y = n-1, n-1
# 남서북동
dx, dy = [1,0,-1,0], [0,-1,0,1]
cur_dir = 1

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

arr[x][y] = n*n

for _ in range(n*n - 1):    
    nx,ny = x + dx[cur_dir], y + dy[cur_dir]

    # 방향전환
    if not in_range(nx,ny) or arr[nx][ny]:
        cur_dir = (cur_dir + 1) % 4
        nx,ny = x + dx[cur_dir], y + dy[cur_dir]

    arr[nx][ny] = arr[x][y] - 1
    x,y = nx,ny

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()