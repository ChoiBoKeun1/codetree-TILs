MAX_N = 50

t = int(input())
n,m = 0,0
marbles = []
marble_cnt = [
    [0] * (MAX_N+1)
    for _ in range(MAX_N+1)
]

dir_mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def in_range(x,y):
    return 0 < x and x <= n and 0 < y and y <= n

# 구슬 한개 움직이기
def move(marble):
    # 상우좌하
    dxs = [-1,0,0,1]
    dys = [0,1,-1,0]

    x,y,cur_dir = marble

    nx = x + dxs[cur_dir]
    ny = y + dys[cur_dir]

    # 1. 다음 위치가 벽이 없는 경우
    if in_range(nx,ny):
        return (nx,ny,cur_dir)

    # 2. 다음 위치가 벽인 경우
    else:
        return (x,y, 3 - cur_dir)

# 모든 구슬 한번 움직이기
def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)

# 구슬이 부딪혔는지 확인
# cnt 배열에서 숫자가 2 이상이면 부딪혔다고 판단.
def check_collapsed(idx):
    x,y,_ = marbles[idx]
    return marble_cnt[x][y] >= 2

# 부딪힌 구슬들을 지우는 함수
def remove_marbles():
    global marbles

    # 1. 각 구슬 위치에 cnt를 증가시킨다
    for x,y,_ in marbles:
        marble_cnt[x][y] += 1

    # 2. 부딪히지 않은 구슬만을 기록
    new_marbles = [
        marble
        for i,marble in enumerate(marbles)
        if not check_collapsed(i)
    ]

    # 3. cnt 다시 초기화
    for x,y,_ in marbles:
        marble_cnt[x][y] -= 1

    # 4. marbles 배열 업데이트
    marbles = new_marbles

def simulate():
    # 모든 구슬을 한번씩 움직인다
    move_all()

    # 움직인 후 충돌한 구슬들을 지운다
    remove_marbles()

for _ in range(t):
    # 새 테스트케이스를 사용하므로
    # 값 초기화
    marbles = []

    n,m = map(int,input().split())
    for _ in range(m):
        x,y,d = tuple(input().split())
        x,y = int(x),int(y)
        marbles.append((x,y,dir_mapper[d]))

    # 시뮬레이션 2n번 진행
    for _ in range(2*n):
        simulate()

    print(len(marbles))