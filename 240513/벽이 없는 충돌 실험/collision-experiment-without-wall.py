COORD_SIZE = 4000
OFFSET = 2000
BLANK = -1

# 테스트케이스 개수 입력
t = int(input())

marbles = []
next_marbles = []

# 겹치는 구슬 확인을 위한 2차원 배열
# 구슬이 겹치는지 확인을 O(1) 에 가능
next_marble_idx = [
    [BLANK] * (COORD_SIZE+1)
    for _ in range(COORD_SIZE+1)
]

cur_time = 0
last_collision_time = -1

mapper = {'U': 0, 'R': 1, 'L': 2, 'D': 3}

def in_range(x,y):
    return 0 <= x and x <= COORD_SIZE and 0 <= y and y <= COORD_SIZE

# 구슬 움직이기
# 1초 후 구슬 위치 구하기
def move(marble):
    dxs = [0,1,-1,0]
    dys = [1,0,0,-1]

    x, y, w, move_dir, num = marble
    nx = x + dxs[move_dir]
    ny = y + dys[move_dir]

    return (nx,ny,w,move_dir,num)

# marble 위치에 구슬이 이미 있는지 확인
# 이미 있다면, 그 구슬의 idx 리턴.
# 없으면, BLANK 리턴 된다.
def find_duplicate_marble(marble):
    x,y,_,_,_ = marble
    return next_marble_idx[x][y]

# 두 구슬 충돌시
# 구슬 하나만 남긴다
# 우선순위 : weight, num
def collide(marble1, marble2):
    _, _, weight1, _, num1 = marble1
    _, _, weight2, _, num2 = marble2

    if weight1 > weight2 or (weight1 == weight2 and num1 > num2):
        return marble1
    else: 
        return marble2

# 
def push_next_marble(marble):
    global last_collision_time

    x,y, _, _, _ = marble

    # 이 구슬이 범위를 벗어나면,
    # 함수 종료  
    if not in_range(x,y):
        return

    idx = find_duplicate_marble(marble)

    # 1. 같은 위치에 구슬이 없다면
    # 그대로 next_marbles 리스트에 추가
    if idx == BLANK:
        next_marbles.append(marble)

        # 겹치는 구슬 확인을 위한
        # next_marble_idx 2차원 배열에 저장
        # [x][y] 에 index를 저장
        next_marble_idx[x][y] = len(next_marbles) -1

    # 2. 같은 위치에 구슬이 있다면
    # 더 영향력 있는 구슬만 남기고
    # last_collision_time을 cur_time으로 update
    else:
        next_marbles[idx] = collide(next_marbles[idx], marble)
        last_collision_time = cur_time

def simulate():
    global marbles, next_marbles

    for marble in marbles:
        # 1. 각 구슬에 대해, 한칸 움직인 이후 위치를 가져온다
        next_marble = move(marble)

        # 2. next_marbles 리스트 업데이트
        push_next_marble(next_marble)
    
    marbles = next_marbles[:]

    # next_marbles, next_marble_idx 배열 초기화
    for x,y,_,_,_ in next_marbles:
        next_marble_idx[x][y] = BLANK
    next_marbles = []

for _ in range(t):
    marbles = []
    last_collision_time = -1

    n = int(input())
    for i in range(1, n+1):
        x,y,w,d = input().split()
        x,y,w = map(int, [x,y,w])

        x,y = 2*x,2*y

        x += OFFSET
        y += OFFSET

        marbles.append( (x,y,w,mapper[d],i) )
    
    for i in range(1, COORD_SIZE +1):
        cur_time = i
        simulate()

    print(last_collision_time)