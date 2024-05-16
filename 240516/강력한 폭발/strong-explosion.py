n = int(input())
arr = []

num_of_bomb = 0

bomb_list = []

ans = 0

EXPLODED = 4

for i in range(n):
    row = list(map(int,input().split()))
    for elem in row:
        if elem == 1:
            num_of_bomb += 1
    arr.append(row)


initial_arr = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        initial_arr[i][j] = arr[i][j]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def clear_arr():
    for i in range(n):
        for j in range(n):
            arr[i][j] = initial_arr[i][j]    

def get_exploded_numbers():
    return sum(
        1
        for i in range(n)
        for j in range(n)
        if arr[i][j] != 0
    )

def recursive(cnt):
    global ans 

    if cnt == num_of_bomb:
        explode_all()
        ans = max(ans,get_exploded_numbers())
        clear_arr()
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                for num in range(1,4):
                    bomb_list.append((i,j,num))
                    recursive(cnt +1)
                    bomb_list.pop()


def explode(x,y,num):
    if num == 1:
        dxs = [0,1,-1,2,-2]
        dys = [0,0,0,0,0]
    elif num == 2:
        dxs = [0,1,0,-1,0]
        dys = [0,0,1,0,-1]
    elif num == 3:
        dxs = [0,1,1,-1,-1]
        dys = [0,1,-1,1,-1]
    
    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx,ny):
            arr[nx][ny] = EXPLODED


def explode_all():
    for x,y,num in bomb_list:
        explode(x,y,num)

recursive(0)
print(ans)