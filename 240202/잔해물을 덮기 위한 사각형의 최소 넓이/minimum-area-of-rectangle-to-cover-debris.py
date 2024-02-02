OFFSET = 1000
MAX_L = 2000

rect1 = tuple(map(int,input().split()))
rect2 = tuple(map(int,input().split()))

x1,y1,x2,y2 = rect1
a1,b1,a2,b2 = rect2

check = [
    [0] * (MAX_L+1)
    for _ in range(MAX_L+1)
]

x1,y1 = x1+OFFSET, y1+OFFSET
x2,y2 = x2+OFFSET, y2+OFFSET

for x in range(x1,x2):
    for y in range(y1,y2):
        check[x][y] = 1

a1,b1 = a1+OFFSET, b1+OFFSET
a2,b2 = a2+OFFSET, b2+OFFSET

for a in range(a1,a2):
    for b in range(b1,b2):
        check[a][b] = 0

min_x, max_x, min_y, max_y = MAX_L, 0, MAX_L, 0
first_rect_exist = False
for x in range(MAX_L+1):
    for y in range(MAX_L+1):
        if check[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

if not first_rect_exist:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(area)