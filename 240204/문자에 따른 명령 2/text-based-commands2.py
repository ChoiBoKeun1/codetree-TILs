s = input()
x,y = 0,0

# 동남서북
dx,dy = [1,0,-1,0],[0,-1,0,1]

move_dir = 3

if s[0] == 'L':
    move_dir = (move_dir -1 + 4) % 4
else:
    move_dir = (move_dir + 1) % 4

x += dx[move_dir]
y += dy[move_dir]

print(x,y)