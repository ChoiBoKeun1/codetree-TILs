n,m,k = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

k -= 1

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def is_fall(cur_i, arr):
    flag = True

    for j in range(k, k+m):
        if arr[cur_i][j] != 1 or arr[cur_i+1][j] != 0:
            flag = False

    return flag

def fall():
    global arr

    tmp = [
        inner[:]
        for inner in arr
    ]

    for i in range(n-1):
        if is_fall(i, tmp):
            for j in range(k,k+m):
                tmp[i][j] = 0
                tmp[i+1][j] = 1

    arr = tmp

# 맨 위에 블록 배치
for j in range(k,k+m):
    arr[0][j] = 1

fall()
print_arr()