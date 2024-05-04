n,m, r,c = map(int,input().split())
r,c = r-1,c-1

arr = [
    [0] * n
    for _ in range(n)
]

dice = [
    [0,5,0],
    [4,6,3],
    [0,2,0]
]

def cur_eye():
    return dice[1][1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def roll(d):
    if d == 'L':
        dice[1] = [7 - cur_eye(), dice[1][0], dice[1][1]]
    elif d == 'R':
        dice[1] = [dice[1][1], dice[1][2], 7 - cur_eye()]
    
    elif d == 'U':
        [dice[0][1],dice[1][1],dice[2][1]] = [7-cur_eye(), dice[0][1], dice[1][1]]

    elif d == 'D':
        [dice[0][1],dice[1][1],dice[2][1]] = [dice[1][1], dice[2][1], 7-cur_eye()]

arr[r][c] = cur_eye()
d_list = map(str,input().split())

for d in d_list:
    if d == 'L':
        direction = 0
    elif d == 'R':
        direction = 1
    elif d == 'U':
        direction = 2
    else:
        direction = 3

    # L,R,U,D
    dxs = [0,0,-1,1]
    dys = [-1,1,0,0]

    next_x = r + dxs[direction]
    next_y = c + dys[direction]

    if not in_range(next_x,next_y):
        continue

    r = next_x
    c = next_y
    roll(d)
    arr[r][c] = cur_eye()

print(sum(map(sum, arr)))