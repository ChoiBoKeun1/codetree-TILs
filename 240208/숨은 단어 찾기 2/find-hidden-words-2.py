n,m = map(int,input().split())
arr = [
    input()
    for _ in range(n)
]

# 남 남서 서 북서 북 북동 동 남동
dxs = [1,1,0,-1,-1,-1,0,1]
dys = [0,-1,-1,-1,0,1,1,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 'L':
            continue
        
        for dx, dy in zip(dxs,dys):
            x,y = i,j
            cnt = 0
            while True:
                nx = x + dx
                ny = y + dy

                if not in_range(nx,ny):
                    break
                if arr[nx][ny] != 'E':
                    break
                cnt += 1
                x,y = nx,ny                 
                
                if cnt == 2:
                    ans += 1
                    break
print(ans)