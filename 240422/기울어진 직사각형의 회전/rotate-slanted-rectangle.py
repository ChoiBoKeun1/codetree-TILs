n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

r,c, m1,m2,m3,m4, d = map(int,input().split())

r,c = r-1, c-1

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()

def simulate(d):
    new_arr = [
        inner_list[:]
        for inner_list in arr
    ]

    # d == 1 일때. 즉 시계방향으로 회전
    if d:
        dxs = [-1,-1,1,1]
        dys = [-1,1,1,-1]
        dirs = [m2,m3,m4,m1]
    
    # d == 0. 즉 반시계 방향으로 회전
    else:
        dxs = [-1,-1,1,1]
        dys = [1,-1,-1,1]
        dirs = [m1,m2,m3,m4]
        
    new_arr[r][c] = arr[r][c]

    cur_x, cur_y = r,c
    next_x, next_y = r,c

    for dx,dy, _dir in zip(dxs,dys, dirs):
        for i in range(_dir):
            next_x = cur_x + dx
            next_y = cur_y + dy

            new_arr[next_x][next_y] = arr[cur_x][cur_y]

            cur_x, cur_y = next_x, next_y
    
    return new_arr

ans = simulate(d)
print_arr(ans)