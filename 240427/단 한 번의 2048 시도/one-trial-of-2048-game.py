n = 4
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
cmd = input()

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()

# 시계방향 90도 회전
def rotate_arr():
    global arr

    tmp = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            tmp[i][j] = arr[n-1-j][i]

    arr = tmp

# 오른쪽으로 shift
def right_shift():
    global arr

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

    arr = tmp

# 오른쪽을 기준으로, 같은 값 2개 합치기
def right_merge():
    global arr

    for i in range(n):
        cur_idx = n-1
        for j in range(n-1, 0, -1):
            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0
    
def simulation(cmd):    
    if cmd == 'R':
        move_dir = 0
    elif cmd == 'U':
        move_dir = 1
    elif cmd == 'L':
        move_dir = 2
    else:
        move_dir = 3
    
    for _ in range(move_dir):
        rotate_arr()

    right_shift()
    right_merge()
    right_shift()

    for _ in range(4 - move_dir):
        rotate_arr()

# main 함수
simulation(cmd)
print_arr()