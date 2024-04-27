n = 4
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
cmd = input()

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()

# 시계방향 90도 회전
def rotate_arr():
    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[j][n-1-i]

    return tmp

# 오른쪽으로 shift
def right_shift():
    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        cur_idx = n-1
        for j in range(n-1, -1, -1):
            if arr[i][j] != 0:
                tmp[i][cur_idx] = arr[i][j]
                cur_idx -= 1

    return tmp

# 오른쪽을 기준으로, 같은 값 2개 합치기
def right_merge():
    for i in range(n):
        cur_idx = n-1
        for j in range(n-1, 0, -1):
            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0
    return arr
    
                
def simulation():
    arr = right_shift()
    arr = right_merge()
    arr = right_shift()

    print_arr(arr)

# main 함수
if cmd == 'R':
    simulation()

elif cmd == 'U':
    arr = rotate_arr()
    simulation()

elif cmd == 'L':
    arr = rotate_arr()
    arr = rotate_arr()
    simulation()

else:
    arr = rotate_arr()
    arr = rotate_arr()
    arr = rotate_arr()
    simulation()