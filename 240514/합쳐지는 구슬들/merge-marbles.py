n,m,t = map(int,input().split())

arr = [
    [0] * n
    for _ in range(n)
]
next_arr = [
    [0] * n
    for _ in range(n)
]

mapper = {'D': 0, 'R':1, 'L': 2, 'U': 3}

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x,y,move_dir):
    dxs = [1,0,0,-1]
    dys = [0,1,-1,0]

    nx = x + dxs[move_dir]
    ny = y + dys[move_dir]

    if not in_range(nx,ny):
        move_dir = 3 - move_dir
    else:
        x,y = nx,ny

    return (x,y,move_dir)

def collision(marble1, marble2):
    w1, move_dir1, num1 = marble1
    w2, move_dir2, num2 = marble2

    if num1 > num2:
        new_dir = move_dir1
        new_num = num1
    else:
        new_dir = move_dir2
        new_num = num2

    new_marble = (w1+w2, new_dir, new_num)
    return new_marble

def push_to_next_arr(x,y,w,move_dir,num):
    if not next_arr[x][y]:
        next_arr[x][y] = (w,move_dir,num)
    
    else:
        next_arr[x][y] = collision((w,move_dir,num), next_arr[x][y])

def move_all():
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                w,move_dir,num = arr[i][j]
                nx,ny,next_dir = move(i,j,move_dir)
                
                push_to_next_arr(nx,ny,w,next_dir,num)

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

def simulate():
    for i in range(n):
        for j in range(n):
            next_arr[i][j] = 0

    move_all()

# main
for i in range(1, m+1):
    r,c,d,w = input().split()
    r,c,w = map(int, [r,c,w])

    arr[r-1][c-1] = (w, mapper[d], i)

for _ in range(t):
    simulate()

num_of_marbles = 0
max_weight = 0

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            w,_,num = arr[i][j]
            max_weight = max(max_weight, w)
            num_of_marbles += 1

print(num_of_marbles, max_weight)