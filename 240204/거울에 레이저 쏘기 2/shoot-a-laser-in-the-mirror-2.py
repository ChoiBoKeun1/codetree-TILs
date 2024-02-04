n = int(input())
arr = [
    input() 
    for _ in range(n)
]

k = int(input())

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

'''
시작방향
  0
3 ㅁ 1
  2
'''
# return : x,y, 시작방향
def initialize(num):
    if num <= n:
        return 0, num-1, 0
    elif num <= 2*n:
        return num-n-1, n-1, 1
    elif num <= 3*n:
        return n-1, n-(num-2*n), 2
    else:
        return n-(num-3*n), 0, 3

'''
dx,dy
          dir=2(-1,0)

dir=1(0,-1)          dir=3(0,1)
       
          dir=0(1,0)
'''
def move(x,y, next_dir):
    dxs = [1,0,-1,0]
    dys = [0,-1,0,1]
    nx,ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir

def simulate(x,y,move_dir):
    move_num = 0
    while in_range(x,y):
        # 방향 전환 0 <-> 1 , 2 <-> 3의 경우. XOR 연산자로 가능하다.
        if arr[x][y] == '/':
            x,y,move_dir = move(x,y,move_dir ^ 1)
        # 방향 전환 0 <-> 3, 1 <-> 2
        else:
            x,y,move_dir = move(x,y,3 - move_dir)
        
        move_num += 1
    
    return move_num

x,y,move_dir = initialize(k)
move_num = simulate(x,y,move_dir)
print(move_num)