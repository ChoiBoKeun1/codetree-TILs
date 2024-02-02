OFFSET = 100
MAX_L = 200

n = int(input())

rect = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

check = [
    [0] * (MAX_L + 1)
    for _ in range(MAX_L + 1)
]

for i, (x1,y1,x2,y2) in enumerate(rect, start=1):
    for x in range(x1,x2):
        for y in range(y1,y2):
            if i % 2 != 0:
                check[x][y] = 1
            else:
                check[x][y] = 2

area = 0
for x in range(MAX_L+1):
    for y in range(MAX_L+1):
        if check[x][y] == 2:
            area += 1

print(area)