import sys

n = int(input())
x,y = map(int,input().split())
x,y = x-1,y-1

arr = [
    input()
    for _ in range(n)
]

visited = [
    [
        [False for _ in range(4)]
        for _ in range(n)
    ] 
    for _ in range(n)
]

cur_x,cur_y = x,y

# cur_dir : 0,1,2,3 오, 아래, 왼, 위
cur_dir = 0

total_time = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# x,y 자리가 벽인가?
def is_wall(x,y):
    return in_range(x,y) and arr[x][y] == '#'

def simulate():
    global cur_x,cur_y
    global cur_dir
    global total_time

    # 만약 현재 위치에서, 이쪽방향으로 간적이 있었다면,
    # 여길 두번째 왔다는 소리니까
    # 탈출이 불가능하다 판단한다.
    if visited[cur_x][cur_y][cur_dir]:
        print(-1)
        sys.exit(0)

    # 이 위치를 방문했다고 마킹.
    visited[cur_x][cur_y][cur_dir] = True
        
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    
    # 다음으로 갈 좌표
    next_x = cur_x + dxs[cur_dir]
    next_y = cur_y + dys[cur_dir]


    # 1. 다음좌표가 벽임

    # 반시계 회전
    if is_wall(next_x,next_y):
        cur_dir = (cur_dir -1 +4) % 4

    # 2. 벽 아님

    # 2-1. 다음으로 갈 좌표가 범위 바깥임
    # 탈출
    elif not in_range(next_x,next_y):
        cur_x, cur_y = next_x, next_y
        total_time += 1
    
    # 2-2, 2-3 다음으로 갈 좌표가 범위 안쪽임
    else:
        # 다음 좌표의 오른쪽에 벽이 있는가를 확인해보자

        # 다음 좌표의 오른쪽 좌표.
        rx = next_x + dxs[(cur_dir +1) % 4]
        ry = next_x + dxs[(cur_dir +1) % 4]

        # 2-2. 다음좌표 오른쪽에 벽이 있음.
        # 해당 방향으로 한칸 이동.
        if is_wall(rx,ry):
            cur_x,cur_y = next_x,next_y
            total_time += 1

        # 2-3. 다음좌표 오른족에 벽 없음
        # 이동 -> 회전 -> 이동. 즉, 현재위치를 rx,ry로 바꾸고, 방향 전환해주면 된다.
        else:
            cur_x, cur_y = rx, ry
            total_time += 2

# 격자를 빠져나올때까지 반복
while in_range(cur_x,cur_y):
    simulate()

print(total_time)