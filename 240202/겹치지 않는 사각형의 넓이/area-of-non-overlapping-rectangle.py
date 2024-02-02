rect = [
    tuple(map(int,input().split())),
    tuple(map(int,input().split()))
]
M = [tuple(map(int,input().split()))]


OFFSET = 1000
MAX_LENGTH = 2000

check = [
    [0] * (MAX_LENGTH + 1)
    for _ in range(MAX_LENGTH + 1)
]

for x1,y1,x2,y2 in rect:
    x1,y1 = x1+OFFSET, y1+OFFSET
    x2,y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            check[x][y] = 1

for x1,y1,x2,y2 in M:
    x1,y1 = x1+OFFSET, y1+OFFSET
    x2,y2 = x2+OFFSET, y2+OFFSET

    for x in range(x1,x2):
        for y in range(y1,y2):
            check[x][y] = 0

area = 0
for x in range(MAX_LENGTH+1):
    for y in range(MAX_LENGTH+1):
        if check[x][y]:
            area += 1

print(area)