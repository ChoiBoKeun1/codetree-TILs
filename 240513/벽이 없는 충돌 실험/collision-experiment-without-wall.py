t = int(input())

COORD_SIZE = 4000
OFFSET = 2000
BLANK = -1

'''
marble = (x, y, weight, d, num)
'''

marbles = []
next_marbles = []
next_marble_idx = [
    [BLANK] * (COORD_SIZE +1)
    for _ in range(COORD_SIZE +1)
]

cur_time = 0
last_collision_time = -1

mapper = {'U': 0, 'R': 1, 'D': 2, 'L': 3}

def in_range(x,y):
    return 0 <= x and x <= COORD_SIZE and 0 <= y and y <= COORD_SIZE

# 구슬이 움직인 위치에 이미 구슬이 있는지를 확인
# 있다면 해당 구슬의 idx, 없으면 BLANK가 리턴된다.
def get_idx_duplicate_marble(marble):
    x, y, _, _, _ = marble
    return next_marble_idx[x][y]

# 구슬 2개가 충돌했을 때
def collision(marble1, marble2):
    _, _, w1, _, num1 = marble1
    _, _, w2, _, num2 = marble2

    if w1 > w2 or (w1 == w2 and num1 > num2):
        return marble1
    else:
        return marble2

def move(marble):
    # 지금까지 썼던 2차원 arr의 row,col을 생각하지 말고,
    # 좌표평면을 생각했을 때의 dxs, dys. 즉 y축이 위아래, x축이 좌우
    dxs = [0,1,0,-1]
    dys = [1,0,-1,0]
    
    x, y, w, move_dir, num = marble

    nx = x + dxs[move_dir]
    ny = y + dys[move_dir]

    return (nx, ny, w, move_dir, num)

# 움직인 구슬이 충돌했는지 확인
def push_to_next_marbles(marble):
    global cur_time, last_collision_time

    x, y, _, _, _ = marble

    if not in_range(x,y):
        return

    # 움직인 구슬의 위치에 이미 구슬이 있는지 확인
    idx = get_idx_duplicate_marble(marble)

    # 1. 없으면, next_marbles 리스트에 이 구슬을 넣고
    # 이 구슬이 next_marbles 리스트의 몇번째 index인지를 확인하기 위해
    # next_marble_idx[x][y]에 index를 넣는다.
    if idx == BLANK:
        next_marbles.append(marble)
        next_marble_idx[x][y] = len(next_marbles) -1

    # 2. 있다면, 더 영향력있는 구슬만 남기고,
    # 가장 최근 충돌 시간을 업데이트 한다.
    else:
        next_marbles[idx] = collision(marble, next_marbles[idx])
        last_collision_time = cur_time

# 모든 구슬을 1번 움직인다.
def simulate():
    global marbles, next_marbles

    # 모든 구슬에 대해 for문
    for marble in marbles:
        # 1. 구슬을 움직이고
        next_marble = move(marble)
        
        # 2. 움직인 구슬들에 대해 충돌을 확인 후 처리
        push_to_next_marbles(next_marble)
    
    # 3. marbles 리스트를 움직인 후로 업데이트
    marbles = next_marbles[:]

    # 4. 사용한 next_marbles, next_marble_idx 리스트 초기화
    for x,y,_,_,_ in next_marbles:
        next_marble_idx[x][y] = BLANK
    next_marbles = []

# main함수
for _ in range(t):
    # 테스트케이스 시작 시, marbles 리스트와 마지막 충돌시간 초기화
    marbles = []
    last_collision_time = -1

    n = int(input())

    for i in range(1, n+1):
        x,y,w,d = input().split()
        x,y,w = map(int, [x,y,w])

        # 문제에서 주어진 조건 : 
        # 2초에 한번씩 움직임 + 중간에 만나도 충돌함
        # 위 2가지 문제를 해결하기 위해
        # 좌표평면을 2배로 늘리고, 1초에 한번씩 움직이는 문제로 바꿔준다 

        # 그것을 위한 주어진 좌표 2배
        x,y = 2*x, 2*y

        
        # 또한 주어진 조건에 x,y 는 -1000 ~ 1000 이고,
        # 좌표 2배를 했기 때문에 -2000 ~ 2000 이다.

        # 배열을 사용할 수 있게 범위를 0 ~ 4000 으로 바꿔준다.
        # 그러므로 OFFSET = 2000 으로 설정하고 더해준다.
        x,y = x+OFFSET, y+OFFSET
        
        marbles.append( (x,y,w,mapper[d],i) )

    # COORD_SIZE = 4000.
    # 모든 구슬들은 (0,0) ~ (4000,4000) 사이에 있기 때문에
    # 한방향으로 직전밖에 할수 없는 구슬들은
    # simulate를 최대치인 4000번 반복하면, 모든 구슬들은 격자 밖으로 빠져나가게 된다.
    # 즉 그 이후로는 simulate 할 필요가 없다.
    for i in range(1, COORD_SIZE +1):
        # 한번 simulate 할때마다 1초씩 늘어난다.
        cur_time = i
        simulate()
    
    print(last_collision_time)