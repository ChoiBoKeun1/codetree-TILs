n = int(input())
dx,dy = [1,0,-1,0], [0,-1,0,1]
x,y = 0,0

for _ in range(n):
    cmd, d = map(str,input().split())
    d = int(d)
    if cmd == 'E':
        x = x + dx[0] * d
        y = y + dy[0] * d    
    elif cmd == 'S':
        x = x + dx[1] * d
        y = y + dy[1] * d
    elif cmd == 'W':
        x = x + dx[2] * d
        y = y + dy[2] * d
    else:
        x = x + dx[3] * d
        y = y + dy[3] * d
print(x,y)