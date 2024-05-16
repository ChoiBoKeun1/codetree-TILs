n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 폭탄의 위치 기록
bomb_pos = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bomb_pos.append((i,j))

# 선택된 폭탄의 type
selected_bomb_types = []

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def copy_arr(arr):
    return [
        [arr[i][j] for i in range(n)]
        for j in range(n)
    ]

def get_exploded_numbers():
    return sum(
        1
        for i in range(n)
        for j in range(n)
        if arr[i][j] != 0
    )

def recursive(cnt):
    if cnt == len(bomb_pos):
        explode_all()
        return

    for bomb_type in range(3):
        selected_bomb_types.append(bomb_type)
        recursive(cnt +1)
        selected_bomb_types.pop()

def explode(x,y,bomb_type):
    dxdy_set = [
        ([-2,-1,1,2], [0,0,0,0]),
        ([-1,1,0,0], [0,0,1,-1]),
        ([-1,-1,1,1], [-1,1,-1,1])
    ]
    dxs, dys = dxdy_set[bomb_type]

    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx,ny) and arr[nx][ny] != 1:
            arr[nx][ny] = 1

def explode_all():
    global ans, arr

    tmp = copy_arr(arr)
    for num in range(len(bomb_pos)):
        x,y = bomb_pos[num]
        bomb_type = selected_bomb_types[num]
        explode(x,y,bomb_type)

    ans = max(ans,get_exploded_numbers())

    # arr 원상복구
    arr = copy_arr(tmp)

ans = 0
recursive(0)
print(ans)