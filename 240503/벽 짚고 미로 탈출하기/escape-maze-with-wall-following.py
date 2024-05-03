n = int(input())
x,y = map(int,input().split())
x,y = x-1,y-1

arr = [
    input()
    for _ in range(n)
]

cur_x,cur_y = x,y
# direction : 0,1,2,3 오, 아래, 왼, 위
direction = 0
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

total_time = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def move():
    global cur_x, cur_y
    global total_time

    cur_x += dxs[direction]
    cur_y += dys[direction]

    total_time += 1


def turn(turn_direction):
    global direction

    # 시계방향 회전
    if turn_direction == 0:
        direction = (direction +1) % 4

    # 반시계방향 회전
    else:
        direction = (direction -1 +4) % 4


def is_wall(x,y):
    # x,y 자리가 벽인가?
    return arr[x][y] == '#'

def is_wall_right(x,y):
    # x,y에서, direction을 기준으로 오른쪽에 벽이 있는가?
    right_hand = (direction+1) % 4
    next_x = x + dxs[right_hand]
    next_y = y + dys[right_hand]
    return arr[next_x][next_y] == '#'

def simulate():
    global cur_x,cur_y
    global direction

    while True:
        # 다음으로 갈 좌표
        next_x = cur_x + dxs[direction]
        next_y = cur_y + dys[direction]

        # 다음으로 갈 좌표가 
        # 범위 바깥임
        # move 후 함수 탈출
        if not in_range(next_x,next_y):
            move()
            return None

        # 다음좌표가 벽임
        # 반시계회전후 move
        if is_wall(next_x,next_y):
            turn(1)
            move()

        # 벽 아님
        # 다음좌표 오른쪽이 벽임
        # move
        elif is_wall_right(next_x,next_y):
            move()

        # 벽 아님
        # 다음좌표 오른쪽 비어있음
        # 이동 후 꺾고 다시 이동
        else:
            move()
            turn(0)
            move()

        # 이동 후, 탈출했는지 확인
        # 탈출했으면 함수 끝
        if not in_range(cur_x,cur_y):
            return None



ans = simulate()
print(total_time)