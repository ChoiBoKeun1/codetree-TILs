from collections import deque
n,m,k = map(int,input().split())

#몸통만 뱀 
one_maps = [ [0]*n for _ in range(n)]

#머리만 이동뱀
head_maps = [ [0]*n for _ in range(n)]

#뱀들의 머리 정보 0인덱스가 머리 그다음부터 몸 

snake = deque()
dxs=[-1,1,0,0]
dys=[0,0,1,-1]
#사과 위치
apple = [ [0]*n for _ in range(n)]


for j in range(m) : 
    x,y= map(int,input().split())
    x-=1
    y-=1
    apple[x][y] = 1 

start_x = 0
start_y = 0
snake.append((start_x,start_y))

def in_range(x,y) : 
    return 0<= x < n and 0<=y<n

# 다음 위치에 뱀머리, 뱀몸통을 업데이트 시킴 
def update_snake(snake) : 
    global one_maps, head_maps
    one_maps = [ [0]*n for _ in range(n)] #맵스 초기화 
    head_maps = [ [0]*n for _ in range(n)] #맵스 초기화 
    for i in range(len(snake)) : 
        a,b = snake[i]
        if i == 0 : 
            head_maps[a][b] = 2 # 2가 머리 
        else : 
            one_maps[a][b] = 1 # 그다음 녀석을 그린다. 
    for x in range(n) : 
        for y in range(n) : 
            if in_body(x,y) : 
                return -1 


def in_body(x,y) : 
    if head_maps[x][y] ==2 and one_maps[x][y] == 1  : 
        return True
    return False

# 뱀 이동 위치 
def move(pos):
    #x,y 는 헤드값이다. 
    x,y = snake[0]
    
    nx,ny = x + dxs[pos], y + dys[pos]
    if not in_range(nx,ny) : 
        return -1 # 격자를 벗어난다. 
    if in_range(nx,ny)  :
        if apple[nx][ny] == 1 : # 사과가있다면 
            apple[nx][ny] = 0 # 0으로 하고
            # snake 길이 그냥 늘리기 
            snake.appendleft((nx,ny))
        else : # 아닐경우 
            snake.appendleft((nx,ny)) # 머리로 등록 .
            snake.pop() #꼬리 자르기 
    #옮기고 난다음, 
    return 0

times = 0
stop_count = False
checked2 = 0

for _ in range(k) :
    d,p = input().split() 
    if d == 'U' : 
        pos = 0
    elif d=='D' : 
        pos = 1 
    elif d == 'R' : 
        pos = 2 
    else : 
        pos = 3 

    p = int(p)
    for power in range(p) : 
        times += 1 
        checked = move(pos) 
        checked2 = update_snake(snake)
        if checked == -1 or checked2 == -1 : #끝내기 
            stop_count = True
            break
    if stop_count == True : 
        break
print(times)