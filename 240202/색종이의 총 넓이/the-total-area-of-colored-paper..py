OFFSET = 100
MAX_L = 200

n = int(input())

rect = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

check = [
    [0] * (MAX_L+1)
    for _ in range(MAX_L+1)
]

for x1,y1 in rect:
    x1,y1 = x1+OFFSET, y1+OFFSET

    for x in range(x1, x1+8):
        for y in range(y1, y1+8):
            check[x][y] = 1

area = 0
for x in range(MAX_L+1):
    for y in range(MAX_L+1):
        if check[x][y]:
            area += 1
print(area)