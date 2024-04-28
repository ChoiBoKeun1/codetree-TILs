n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()

def get_row(col):
    for i in range(n):
        if arr[i][col] != 0:
            return i

    return -1

def bomb(r,c):
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    boom_range = arr[r][c]
    
    arr[r][c] = 0
    
    for dx,dy in zip(dxs,dys):    
        cur_x, cur_y = r,c
        for _ in range(boom_range-1):
            cur_x += dx
            cur_y += dy

            if in_range(cur_x,cur_y):
                arr[cur_x][cur_y] = 0

def fall():
    global arr

    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for j in range(n):
        cur_i = n-1
        for i in range(n-1,-1,-1):
            if arr[i][j] != 0:
                tmp[cur_i][j] = arr[i][j]
                cur_i -= 1
    
    arr = tmp

for _ in range(m):
    c = int(input())
    c -= 1

    r = get_row(c)
    if r == -1:
        continue
    
    bomb(r,c)
    fall()

print_arr()