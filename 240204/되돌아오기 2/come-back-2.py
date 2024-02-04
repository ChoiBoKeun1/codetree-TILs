s = input()

x,y = 0,0
# 동남서북
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cur_dir = 3

ans = 0
isBack = False
for elem in s:
    if elem == 'L':
        cur_dir = (cur_dir - 1 + 4) % 4
    elif elem == 'R':
        cur_dir = (cur_dir + 1) % 4
    else:
        x += dx[cur_dir]
        y += dy[cur_dir]
    
    ans += 1
    if x == 0 and y == 0:
        isBack = True
        break

if not isBack:
    ans = -1

print(ans)