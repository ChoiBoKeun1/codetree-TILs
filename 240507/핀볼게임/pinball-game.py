n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

total_time = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate(x,y, dx,dy):
    global total_time
    total_time = 1

    if arr[x][y] == 1:
        dx,dy = -dy, -dx
    elif arr[x][y] == 2:
        dx,dy = dy,dx
    
    while True:
        total_time += 1

        nx = x + dx
        ny = y + dy

        if not in_range(nx,ny):
            break

        # / 를 만난 경우
        # 방향이 꺾이면서 부호도 달라져야 한다
        if arr[nx][ny] == 1:
            dx,dy = -dy, -dx
        
        # \ 를 만난 경우
        # 방향이 꺾이지만 부호는 그대로
        elif arr[nx][ny] == 2:
            dx,dy = dy,dx

        x,y = nx,ny

ans = 0

# 위에서 아래로
for j in range(n):
    start_x,start_y = 0,j
    dx,dy = 1,0
    
    simulate(start_x,start_y, dx,dy)
    ans = max(ans,total_time)

# 왼쪽에서 오른쪽으로
for i in range(n):
    start_x,start_y = i,0
    dx,dy = 0,1

    simulate(start_x,start_y,dx,dy)
    ans = max(ans,total_time)

# 왼쪽에서 오른쪽으로
for i in range(n):
    start_x,start_y = i,n-1
    dx,dy = 0,-1

    simulate(start_x,start_y,dx,dy)   
    ans = max(ans,total_time)

# 아래에서 위로
for j in range(n):
    start_x,start_y = n-1,j
    dx,dy = -1,0

    simulate(start_x,start_y,dx,dy)
    ans = max(ans,total_time)

print(ans)