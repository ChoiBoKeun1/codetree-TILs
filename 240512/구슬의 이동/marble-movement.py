# 첫번째 입력
n,m,t,k = map(int, input().split())
grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def next_pos(x,y, vnum, move_dir):
    dxs = [-1,0,0,1]
    dys = [0,1,-1,0]

    for _ in range(vnum):
        nx = x + dxs[move_dir]
        ny = y + dys[move_dir]

        if not in_range(nx,ny):
            move_dir = 3 - move_dir

            nx = x + dxs[move_dir]
            ny = y + dys[move_dir]

        x,y = nx,ny

    return (x,y,move_dir)

def move_all():
    for x in range(n):
        for y in range(n):
            for v, num, move_dir in grid[x][y]:
                next_x,next_y,next_dir = next_pos(x,y,v,move_dir)
                next_grid[next_x][next_y].append((v,num,next_dir))

def select_marbles():
    for i in range(n):
        for j in range(n):
            if len(next_grid[i][j]) >= k:
                # 각 칸을 정렬한다
                # 우선순위 1번 v
                # 우선순위 2번 num
                # 그것을 위한 x[0],x[1] 내림차순 정렬
                next_grid[i][j].sort(key=lambda x: (-x[0], -x[1]))
                
                # 각 칸에 구슬 개수가 k보다 크면 계속 pop.
                while len(next_grid[i][j]) > k:
                    next_grid[i][j].pop()

def simulate():
    # 1. next grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []

    # 2. 모든 구슬을 움직인다
    move_all()

    # 3. 각 칸마다, 구슬이 최대 k개만 있도록 조정한다.
    select_marbles()

    # 4. next grid 값을 grid로 옮긴다.
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

dir_mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

# 두번째 입력
for i in range(1, m+1):
    r,c,d,v = tuple(input().split())
    r,c,v = tuple(map(int, [r,c,v]))

    grid[r-1][c-1].append((v, i, dir_mapper[d]))

# t초 동안 시뮬레이션
for _ in range(t):
    simulate()

ans = sum([
    len(grid[i][j])
    for i in range(n)
    for j in range(n)
])
print(ans)