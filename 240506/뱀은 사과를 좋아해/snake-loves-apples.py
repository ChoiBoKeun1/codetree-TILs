n,m,k = map(int,input().split())
apple = [
    [False for _ in range(n+1)]
    for _ in range(n+1)
]

# 뱀. snake[0]에는 항상 머리가 있다.
snake = [(1,1)]
total_time = 0

dir_mapper = {
    'D': 0,
    'R': 1,
    'U': 2,
    'L': 3
}

# x,y가 범위 안에 있는가
def in_range(x,y):
    return 0 < x and x <= n and 0 < y and y <= n

# 뱀이 꼬였는지 확인
def is_twisted(new_head):
    return new_head in snake

# 새 머리 추가
def push_front(new_head):
    if is_twisted(new_head):
        return False

    snake.insert(0, new_head)

    return True

# 꼬리 지우기
def pop_back():
    snake.pop()

# 뱀 움직이기
def move_snake(nx,ny):
    # 움직일 위치에 사과가 있다면
    # 사과 먹고
    # 머리 추가, 꼬리 삭제 X
    if apple[nx][ny]:
        # 사과 먹기
        apple[nx][ny] = False

        # 머리 추가.
        # 늘어난 머리때문에 몸이 꼬이면 False 리턴
        if not push_front((nx,ny)):
            return False

    # 사과가 없으면
    # 머리 추가, 꼬리 삭제
    else:
        # 꼬리 삭제
        pop_back()

        # 머리 추가.
        # 늘어난 머리때문에 몸이 꼬이면 False 리턴
        if not push_front((nx,ny)):
            return False

    return True

# move_dir 방향으로 num번 움직인다
def move(move_dir, num):
    global total_time

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    for _ in range(num):
        total_time += 1

        x,y = snake[0]

        nx = x + dxs[move_dir]
        ny = y + dys[move_dir]

        # 다음 위치로 갈수 없다면
        # 게임 종료
        if not in_range(nx,ny):
            return False

        # 뱀을 한칸 움직인다
        # 움직였는데 몸이 꼬였다면, 게임 종료
        if not move_snake(nx,ny):
            return False

    return True

for _ in range(m):
    x,y = map(int,input().split())
    apple[x][y] = True

for _ in range(k):
    d,p = input().split()
    p = int(p)

    if not move(dir_mapper[d],p):
        break

print(total_time)