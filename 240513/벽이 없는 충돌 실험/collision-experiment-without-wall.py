mapper = {
    "U": 0,
    "R": 1,
    "D": 2,
    "L": 3
}

marbles, record = None, None
grid = [[None for _ in range(4001)] for __ in range(4001)]
OFFSET_1, OFFSET_2 = 1000, 2
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
coords = []

# 구슬들을 움직이는 함수
def move():
    global marbles, coords
    has_collided = False
    coords.clear()

    for i in range(len(marbles)):
        num, y, x, w, d = marbles[i]
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= 4001 or ny < 0 or ny >= 4001:
            continue

        # 나중에 grid 배열 초기화할때 기록한 부분만 지우기 위해 따로 좌표 기억해두기    
        if grid[nx][ny] == None:
            grid[nx][ny] = [num, ny, nx, w, d]
            coords.append((nx, ny))
        else:
            has_collided = True
            if grid[nx][ny][3] > w:
                continue
            if grid[nx][ny][3] == w and grid[nx][ny][0] > num:
                continue
            grid[nx][ny] = [num, ny, nx, w, d]

    marbles.clear()
    for x, y in coords:
        marbles.append(grid[x][y])
        grid[x][y] = None

    return has_collided   


T = int(input())
for _ in range(T):
    N = int(input())
    marbles, record = [], -1
    for i in range(N):
        marbles.append(
            [i+1] + \
            list(map(lambda x: (int(x[1])+OFFSET_1)*OFFSET_2 if x[0]==0 or x[0]==1 \
                        else int(x[1]) if x[0]==2 \
                        else mapper[x[1]], enumerate(input().split())))
        )

    for second in range(4001):
        if move():
            record = second+1

    print(record)