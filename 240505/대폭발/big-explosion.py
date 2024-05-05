n,m,r,c = map(int,input().split())
r,c = r-1,c-1

arr = [
    [0] * n
    for _ in range(n)
]

BOMB = 1
bomb_list = list()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def print_arr():
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
        print()

def get_ans():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                cnt += 1
    return cnt

time = 0
dxs = [1,0,-1,0]
dys = [0,1,0,-1]

bomb_list.append((r,c))
arr[r][c] = BOMB

while time < m:
    time += 1

    new_bomb_pos = 2 ** (time-1)

    tmp_list = bomb_list[:]
    for bomb in tmp_list:
        cur_x, cur_y = bomb

        for dx,dy in zip(dxs,dys):
            nx = cur_x + dx * new_bomb_pos
            ny = cur_y + dy * new_bomb_pos

            if in_range(nx,ny):
                arr[nx][ny] = BOMB
                bomb_list.append((nx,ny))

print(get_ans())