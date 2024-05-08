n,m,t = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

cnt = [
    [0] * n
    for _ in range(n)
]

next_cnt = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    r,c = map(int,input().split())
    cnt[r-1][c-1] = 1

#############################
def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def clear_arr(arr):
    for i in range(n):
        for j in range(n):
            arr[i][j] = 0

    return arr

def get_next_pos(x,y):
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]

    max_val = 0
    max_val_x = x
    max_val_y = y

    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx,ny):
            if max_val < arr[nx][ny]:
                max_val = arr[nx][ny]
                max_val_x = nx
                max_val_y = ny
    
    return (max_val_x,max_val_y)

def move(x,y):    
    next_x, next_y = get_next_pos(x,y)

    next_cnt[next_x][next_y] += 1

def move_all():
    global cnt, next_cnt

    next_cnt = clear_arr(next_cnt)

    for i in range(n):
        for j in range(n):
            if cnt[i][j] == 1:
                move(i,j)

    for i in range(n):
        for j in range(n):
            cnt[i][j] = next_cnt[i][j]

#############################

for _ in range(t):
    move_all()

ans = 0
for i in range(n):
    for j in range(n):
        if cnt[i][j] == 1:
            ans += 1

print(ans)