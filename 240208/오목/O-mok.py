import sys

n = 19
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# 8방향
# 남 남동 동 북동 북 북서 서 남서
dxs = [1,1,0,-1,-1,-1,0,1]
dys = [0,1,1,1,0,-1,-1,-1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        
        for dx,dy in zip(dxs,dys):
            cnt = 1
            cur_x, cur_y = i, j

            while True:
                nx, ny = cur_x + dx, cur_y + dy
                if not in_range(nx,ny):
                    break
                if arr[nx][ny] != arr[i][j]:
                    break
                cnt += 1
                cur_x, cur_y = nx, ny
            
            if cnt == 5:
                print(arr[i][j])
                print(i + 2*dx + 1, j + 2*dy + 1)
                sys.exit()
print(0)