n,t = map(int,input().split())
r,c,d = map(str,input().split())

r,c = int(r), int(c)

# 동남북서
dx = [1,0,0,-1]
dy = [0,1,-1,0]

# mapper
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

def in_range(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= n

move_dir = mapper[d]
for _ in range(1, t + 1):
    nx = c + dx[move_dir]
    ny = r + dy[move_dir]
    if not in_range(nx, ny):
        move_dir = (3 - move_dir)
    else:
        c,r = c + dx[move_dir] , r + dy[move_dir]

print(r,c)