n = int(input())
# 동남서북
dx,dy = [1,0,-1,0], [0,-1,0,1]
x,y = 0,0

for _ in range(n):
    cmd, d = map(str,input().split())
    d = int(d)
    if cmd == 'E':
        move_dir = 0    
    elif cmd == 'S':
        move_dir = 1
    elif cmd == 'W':
        move_dir = 2
    else:
        move_dir = 3

    x += dx[move_dir] * d
    y += dy[move_dir] * d

print(x,y)