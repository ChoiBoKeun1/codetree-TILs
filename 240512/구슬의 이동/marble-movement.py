# 첫번째 줄 입력
n,m,t,k = map(int,input().split())

grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]
next_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

dir_mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

# 두번째 줄 입력
for i in range(1,m+1):
    r,c,d,v = input().split()
    r,c,v = map(int, [r,c,v])
    grid[r-1][c-1].append((v,i,dir_mapper[d]))

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def next_pos(x,y,vnum,move_dir):
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

# 모든 구슬 움직이기
def move_all():
    for x in range(n):
        for y in range(n):
            for v,num,move_dir in grid[x][y]:
                nx,ny,next_dir = next_pos(x,y,v,move_dir)
                next_grid[nx][ny].append((v,num,next_dir))

# 모든 칸을 확인,
# k보다 많은 구슬들이 한 칸에 있다면
# 우선순위에 따라 구슬을 제거
def remove_marbles():
    for i in range(n):
        for j in range(n):
            # 만약 이 칸에 k보다 많은 구슬들이 있다면
            # 우선순위 : v, num
            # 즉, v와 num 을 기준으로 내림차순 정렬한다.
            if len(next_grid[i][j]) > k:
                next_grid[i][j].sort(key=lambda x: (-x[0], -x[1]))

                # 정렬 후, next_grid[i][j] 리스트의 길이가 k가 될때까지 pop 해준다.
                while(len(next_grid[i][j]) > k):
                    next_grid[i][j].pop()
                next_grid[i][j].pop()


def simulate():
    # 1. next_grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []
    
    # 2. 구슬 움직이기
    move_all()

    # 3. 한칸에 k보다 많은 수의 구슬이 있다면 제거
    remove_marbles()

    # 4. grid를 next_grid의 값으로 update
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

# main 함수
# t초 동안 시뮬레이션
for _ in range(t):
    simulate()

ans = sum(
    len(grid[i][j])
    for i in range(n)
    for j in range(n)
)
print(ans)