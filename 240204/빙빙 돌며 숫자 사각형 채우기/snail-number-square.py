n,m = map(int,input().split())

arr = [
    [0] * m
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < m and 0 <= y and y < n

# 동남서북
dx, dy = [1,0,-1,0], [0,1,0,-1]

x,y = 0,0
move_dir = 0

cnt = 1
for _ in range(n):
    for _ in range(m):
        arr[y][x] = cnt
        nx, ny = x + dx[move_dir], y + dy[move_dir]
        
        # 1. 범위 바깥으로 나감 -> 방향 전환
        # 또는 2. 이미 출력한 부분임 -> 방향 전환
        if not in_range(nx, ny) or arr[ny][nx]:
            move_dir = (move_dir + 1) % 4
            nx, ny = x + dx[move_dir], y + dy[move_dir]

        x,y = nx,ny
        cnt += 1
        
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()