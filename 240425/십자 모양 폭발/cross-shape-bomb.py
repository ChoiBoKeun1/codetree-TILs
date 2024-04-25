n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def bomb(r,c):
    num = arr[r][c]

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    arr[r][c] = 0
    
    for dx, dy in zip(dxs,dys):
        cur_x,cur_y = r,c
        for _ in range(num-1):
            cur_x += dx
            cur_y += dy
            
            if in_range(cur_x,cur_y):
                arr[cur_x][cur_y] = 0

def shift(arr):
    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for j in range(n):
        
        tmp_row = n-1
        for i in range(n-1,-1,-1):
            if arr[i][j] != 0:
                tmp[tmp_row][j] = arr[i][j]
                tmp_row -= 1
    return tmp            


r,c = map(int,input().split())
r,c = r-1,c-1

bomb(r,c)

print_arr(shift(arr))