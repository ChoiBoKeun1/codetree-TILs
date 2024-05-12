n,m,t,k = map(int,input().split())

arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

next_arr = [
    [[] for _ in range(n)]
    for _ in range(n)
]

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

def Print():
    for i in range(n):
        for j in range(n):
            for k in range(len(arr[i][j])):
                print(len(arr[i][j]), end=' ')

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def next_pos(x,y, move_dir, v):
    dxs = [-1,0,0,1]
    dys = [0,1,-1,0]

    while v:
        nx = x + dxs[move_dir]
        ny = y + dys[move_dir]

        if not in_range(nx,ny):
            move_dir = 3 - move_dir
            
            nx = x + dxs[move_dir]
            ny = y + dys[move_dir]
        
        x,y = nx,ny
        v -= 1

    return (x,y,move_dir)

def move_all():
    for r in range(n):
        for c in range(n):
            for i in range(len(arr[r][c])):
                v, num, move_dir = arr[r][c][i]

                next_x,next_y, next_dir = next_pos(r,c, move_dir, (-1) * v)
                next_arr[next_x][next_y].append((v,num,next_dir))

def select_marbles():
    for r in range(n):
        for j in range(n):
            if len(next_arr[r][c]) >= k:
                next_arr[r][c].sort()
                while len(next_arr[r][c]) > k:
                    next_arr[r][c].pop()

def simulate():
    for i in range(n):
        for j in range(n):
            next_arr[i][j].clear()

    move_all()

    select_marbles()

    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

for i in range(m):
    r,c,d,v = input().split()
    r,c,v = int(r),int(c),int(v)

    arr[r-1][c-1].append(
        ( (-1)*v, (-1)*(i+1), mapper[d] )
    )

while t:
    simulate()

    t -= 1

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(arr[i][j])
print(ans)