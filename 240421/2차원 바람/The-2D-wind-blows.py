n,m,q = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 2차원배열 출력
def print_arr(arr):
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()

# 시계방향 rotate
def rotate(r1,c1, r2,c2):
    tmp1 = arr[r1][c2]
    for j in range(c2, c1, -1):
        arr[r1][j] = arr[r1][j-1]
    
    tmp2 = arr[r2][c2]
    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i-1][c2]
    
    tmp3 = arr[r2][c1]
    for j in range(c1, c2):
        arr[r2][j] = arr[r2][j+1]

    for i in range(r1, r2-1):
        arr[i][c1] = arr[i+1][c1]

    arr[r1+1][c2] = tmp1
    arr[r2][c2-1] = tmp2
    arr[r2-1][c1] = tmp3

# 범위 check
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

# x,y와 인접한 숫자들과의 평균값을 계산
def get_block_avg(arr, x,y):
    dxs = [0,1,-1,0,0]
    dys = [0,0,0,1,-1]

    new_arr = [
        arr[x+dx][y+dy]
        for dx,dy in zip(dxs,dys)
        if in_range(x+dx, y+dy)
    ]

    return sum(new_arr) // len(new_arr)

# 새 값을 계산한 2차원 배열을 구한다
def get_new_arr(r1,c1, r2,c2):
    new_arr = [inner_list[:] for inner_list in arr]
    
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            new_arr[i][j] = get_block_avg(arr, i, j)
    
    return new_arr


# main
for _ in range(q):
    r1,c1, r2,c2 = map(int,input().split())
    r1,c1, r2,c2 = r1-1,c1-1, r2-1,c2-1

    # 회전
    rotate(r1,c1,r2,c2)
    # 값 갱신
    arr = get_new_arr(r1,c1, r2,c2)

# 출력
print_arr(arr)