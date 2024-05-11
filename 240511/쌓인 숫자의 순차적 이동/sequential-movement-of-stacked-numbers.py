# 입력
n,m = map(int,input().split())
arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

def get_pos(move_num):
    for i in range(n):
        for j in range(n):
            for num in arr[i][j]:
                if num == move_num:
                    return (i,j)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# 다음 위치 반환
def next_pos(pos):
    dxs = [-1,-1,-1,0,0,1,1,1]
    dys = [-1,0,1,-1,1,-1,0,1]

    x,y = pos

    max_val = -1
    max_pos = (-1,-1)

    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx,ny):
            for num in arr[nx][ny]:
                if num > max_val:
                    max_val = num
                    max_pos = (nx,ny)

    return max_pos

def move(pos, next_pos, move_num):
    x,y = pos
    nx,ny = next_pos
    
    # 1. (x,y)의 move_num 위에 있는 숫자들을 
    #    (nx,ny) 로 옮긴다
    to_move = False
    for num in arr[x][y]:
        if num == move_num:
            to_move = True
        
        if to_move:
            arr[nx][ny].append(num)

    # 2. (x,y)에 있던 숫자들 중
    #    움직인 숫자들을 전부 지운다
    while arr[x][y][-1] != move_num:
        arr[x][y].pop()
    arr[x][y].pop()

def simulate(move_num):
    pos = get_pos(move_num)
    max_pos = next_pos(pos)
    if max_pos != (-1,-1):
        move(pos, max_pos, move_num)

for i in range(n):
    given_row = list(map(int,input().split()))
    for j, num in enumerate(given_row):
        arr[i][j].append(num)

move_nums = list(map(int,input().split()))
for move_num in move_nums:
    simulate(move_num)

for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            print("None",end='')
        else:
            for num in arr[i][j][::-1]:
                print(num, end=' ')
        print()