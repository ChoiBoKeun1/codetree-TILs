n,m, r,c = map(int,input().split())
r,c = r-1,c-1

arr = [
    [0] * n
    for _ in range(n)
]

moves = input().split()

# 윗면, 앞면, 오른쪽면
up,front,right = 1,2,3

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# 다음 위치를 구한다
def next_pos(x,y, move_dir):
    # R,L,U,D 순서
    dxs = [0,0,-1,1]
    dys = [1,-1,0,0]

    nx = x + dxs[move_dir]
    ny = y + dys[move_dir]

    if in_range(nx,ny):
        return (nx,ny)
    else:
        return (-1,-1)

def simulate(move_dir):
    global r,c
    global up,front,right

    # move_dir방향으로 굴렸을때 위치
    nx,ny = next_pos(r,c,move_dir)
    # 굴리는게 불가능할때 : 함수 종료
    if (nx,ny) == (-1,-1):
        return
    
    # 위치 이동
    r,c = nx,ny

    # 주사위면 위치 조정    
    # R,L,U,D
    if move_dir == 0:
        up,front,right = 7 - right, front, up
    elif move_dir == 1:
        up,front,right = right, front, 7 - up
    elif move_dir == 2:
        up,front,right = front, 7 - up, right
    else:
        up,front,right = 7 - front, up, right

    # 바닥 숫자 변경후 arr에 찍기
    bottom = 7 - up
    arr[r][c] = bottom

dir_mapper = {
    'R': 0,
    'L': 1,
    'U': 2,
    'D': 3
}

# main
arr[r][c] = 6
for move_dir in moves:
    simulate(dir_mapper[move_dir])

print(sum(map(sum, arr)))