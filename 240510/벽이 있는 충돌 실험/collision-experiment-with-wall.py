t = int(input())

dir_mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

dxs = [1,0,-1,0]
dys = [0,1,0,-1]

def print_arr(arr):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(arr[i][j],end=' ')
        print()
    print()

def in_range(x,y):
    return 0 < x and x <= n and 0 < y and y <= n

def turn(cur_dir):
    return (cur_dir +2) % 4

def get_ans(arr):
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j] != -1:
                ans += 1
    return ans

# main
for _ in range(t):
    n,m = map(int,input().split())

    arr = [
        [-1] * (n+1)
        for _ in range(n+1)
    ]

    for _ in range(m):
        x,y,d = tuple(input().split())
        x,y = int(x),int(y)

        arr[x][y] = dir_mapper[d]
    
    not_collapsed_cnt = 0

    while True:
        is_collapsed = False

        cnt = [
            [0] * (n+1)
            for _ in range(n+1)
        ]

        next_arr = [
            [-1] * (n+1)
            for _ in range(n+1)
        ]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if arr[i][j] != -1:
                    cur_dir = arr[i][j]
                    nx = i + dxs[cur_dir]
                    ny = j + dys[cur_dir]

                    if in_range(nx,ny):
                        next_arr[nx][ny] = cur_dir
                        cnt[nx][ny] += 1

                    else:
                        next_arr[i][j] = turn(cur_dir)
                        cnt[i][j] += 1

        for i in range(1,n+1):
            for j in range(1,n+1):
                if cnt[i][j] > 1:
                    next_arr[i][j] = -1
                    is_collapsed = True

                arr[i][j] = next_arr[i][j]

        if not is_collapsed:
            not_collapsed_cnt += 1

        if not_collapsed_cnt > n:
            break

    print(get_ans(arr))