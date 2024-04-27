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
            tmp[i][j] = arr[j][n-1-i]

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
    
    
                
def simulation():
    right_shift()
    right_merge()
    right_shift()



# main 함수
if cmd == 'R':
    simulation()

elif cmd == 'D':
    rotate_arr()
    simulation()
    rotate_arr()
    rotate_arr()
    rotate_arr()
    

elif cmd == 'L':
    rotate_arr()
    rotate_arr()
    simulation()
    rotate_arr()
    rotate_arr()

else:
    rotate_arr()
    rotate_arr()
    rotate_arr()
    simulation()
    rotate_arr()

print_arr()