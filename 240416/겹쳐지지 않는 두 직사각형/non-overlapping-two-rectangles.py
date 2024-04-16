import sys

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 빈 board
board = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

def draw(x1,y1,x2,y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            board[i][j] += 1

def check_board():
    # 동일한 칸을 2개의 직사각형이 모두 포함한다면
    # 겹친다. True 리턴.
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

# 두 직사각형이 겹치는지 확인한다
# 겹치면 True. 안겹치면 False
def overlapped(x1,y1,x2,y2, x3,y3, x4,y4):
    clear_board()
    draw(x1,y1, x2,y2)
    draw(x3,y3, x4,y4)
    return check_board()

# 직사각형 합
def rect_sum(x1,y1, x2,y2):
    return sum([
        arr[i][j]
        for i in range(x1, x2+1)
        for j in range(y1, y2+1)
    ])

# 첫 직사각형 x1,y1,x2,y2 가 주어졌을 때,
# 두번째 직사각형(i,j,k,l)을 잘 잡아서
# 최대 합을 반환한다.
def find(x1,y1,x2,y2):
    max_sum = -sys.maxsize

    # 가능한 모든 직사각형
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    # 두 직사각형이 겹치지 않을 때,
                    # 합을 구한다
                    if not overlapped(x1,y1,x2,y2, i,j,k,l):
                        max_sum = max(max_sum, rect_sum(x1,y1,x2,y2) + rect_sum(i,j,k,l))
    return max_sum

ans = -sys.maxsize

# (i,j), (k,l)을 양쪽 꼭지점으로 하는
# 첫번째 직사각형을 정하여
# 그 중 최댓값을 찾아 반환
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                ans = max(ans, find(i,j,k,l))

print(ans)