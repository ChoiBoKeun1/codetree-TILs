OFFSET = 1000
MAX_L = 2000

rect1 = tuple(map(int,input().split()))
rect2 = tuple(map(int,input().split()))


check = [
    [0] * (MAX_L+1)
    for _ in range(MAX_L+1)
]

x1,y1,x2,y2 = rect1
x1,y1 = x1+OFFSET, y1+OFFSET
x2,y2 = x2+OFFSET, y2+OFFSET

for x in range(x1,x2):
    for y in range(y1,y2):
        check[x][y] = 1

x1,y1,x2,y2 = rect2
x1,y1 = x1+OFFSET, y1+OFFSET
x2,y2 = x2+OFFSET, y2+OFFSET

for x in range(x1,x2):
    for y in range(y1,y2):
        if check[x][y] == 1:
            check[x][y] = 2
        else:
            check[x][y] = 0

area = 0
for x in range(MAX_L+1):
    for y in range(MAX_L+1):
        if check[x][y] == 1 or check[x][y] == 2:
            area += 1
            
print(area)