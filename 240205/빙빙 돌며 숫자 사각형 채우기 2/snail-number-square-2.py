n,m = map(int,input().split())

arr = [
    [0] * m
    for _ in range(n)
]
# 남서북동
dx,dy = [1,0,-1,0], [0,-1,0,1]
cur_dir = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

x,y = 0,0
cnt = 1
for i in range(n):
    for j in range(m):
        arr[x][y] = cnt 
        
        # 다음 idx 계산
        nx,ny = x + dx[cur_dir], y + dy[cur_dir]

        # 범위 바깥 or 이미 있는 경우
        # 방향 전환후 다시 계산
        if not in_range(nx,ny) or arr[nx][ny]:
            cur_dir = (cur_dir -1 + 4) % 4
            nx,ny = x + dx[cur_dir], y + dy[cur_dir]
        
        cnt += 1
        # 다음 좌표를 설정
        x,y = nx,ny
        
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()