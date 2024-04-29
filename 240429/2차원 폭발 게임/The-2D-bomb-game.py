n,m,k = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def count_bomb():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                cnt += 1
    return cnt

def get_end_idx(start_idx, cur_num, col):
    for i in range(start_idx+1, n):
        if arr[i][col] != cur_num:
            return i-1
    
    return n-1

def boom():
    while True:
        did_explode = False

        for j in range(n):
            cur_idx = 0
            
            while cur_idx < n :
                cur_num = arr[cur_idx][j]
                end_idx = get_end_idx(cur_idx, cur_num, j)
                
                if cur_num == 0:
                    cur_idx = end_idx + 1

                elif end_idx - cur_idx + 1 >= m:
                    for l in range(cur_idx, end_idx+1):
                        arr[l][j] = 0
                    did_explode = True

                else:
                    cur_idx = end_idx + 1

        if not did_explode:
            break
        else:
            fall()

def fall():
    global arr

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

    arr = tmp

def rotate():
    global arr

    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-j-1][i]

    arr = tmp

def boom_and_rotate():
    boom()

    rotate()
    fall()
   
    boom()
    
    
for _ in range(k):
    boom_and_rotate()

ans = count_bomb()

print(ans)