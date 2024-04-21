n,m,q = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def print_arr(arr):
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()

# 시계방향 shift
def shift(r1,c1, r2,c2):
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

def get_block_sum(arr, i,j):
    _sum = 0
    
    _sum += arr[i][j]
    cnt = 1
    
    if i-1 >= 0:
        _sum += arr[i-1][j]
        cnt += 1
    if i+1 <= n-1:
        _sum += arr[i+1][j]
        cnt += 1
    if j-1 >= 0:
        _sum += arr[i][j-1]
        cnt += 1
    if j+1 <= m-1:
        _sum += arr[i][j+1]
        cnt += 1

    return _sum // cnt

def get_avg(r1,c1, r2,c2):
    new_arr = [inner_list[:] for inner_list in arr]
    
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            new_arr[i][j] = get_block_sum(arr, i, j)
    
    return new_arr

for _ in range(q):
    r1,c1, r2,c2 = map(int,input().split())
    r1,c1, r2,c2 = r1-1,c1-1, r2-1,c2-1

    shift(r1,c1,r2,c2)
    
    arr = get_avg(r1,c1, r2,c2)

print_arr(arr)