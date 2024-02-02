OFFSET = 1000
MAX_L = 2000

rect1 = tuple(map(int,input().split()))
rect2 = tuple(map(int,input().split()))

x1,y1,x2,y2 = rect1
a1,b1,a2,b2 = rect2

if x1 >= a1 and x2 <= a2 and y1 >= b1 and y2 <= b2:
    print(0)
else:
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

    for x in range(a1,a2):
        for y in range(b1,b2):
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