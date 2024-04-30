n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def fall(arr):
    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for j in range(n):
        cur_idx = n-1
        for i in range(n-1,-1,-1):
            if arr[i][j] != 0:
                tmp[cur_idx][j] = arr[i][j]
                cur_idx -= 1

    return tmp

def boom(r,c):
    tmp = [
        inner[:]
        for inner in arr
    ]

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]
    
    bomb_range = arr[r][c]

    tmp[r][c] = 0
    
    for dx, dy in zip(dxs,dys):
        cur_x, cur_y = r,c

        for _ in range(bomb_range-1):
            cur_x += dx
            cur_y += dy

            if in_range(cur_x, cur_y):
                tmp[cur_x][cur_y] = 0


    fallen_arr = fall(tmp)
    return fallen_arr

def check_adj(arr):
    cnt = 0

    for i in range(n):
        for j in range(n-1):
            if arr[i][j] != 0 and arr[i][j] == arr[i][j+1]:
                cnt += 1

    for j in range(n):
        for i in range(n-1):
            if arr[i][j] != 0 and arr[i][j] == arr[i+1][j]:
                cnt += 1

    #print_arr(arr)
    #print(cnt)

    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,check_adj(boom(i,j)))

print(ans)