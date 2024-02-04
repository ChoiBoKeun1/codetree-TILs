n = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

x,y = 0,0
isBack = False
ans = 0
for _ in range(n):
    cmd, t = map(str, input().split())
    t = int(t)

    for _ in range(t):
        x += dx[mapper[cmd]]
        y += dy[mapper[cmd]]
        
        if (x,y) == (0,0):
            isBack = True
            break
        
        ans += 1

    if isBack:
        break

if not isBack:
    ans = -1

print(ans)