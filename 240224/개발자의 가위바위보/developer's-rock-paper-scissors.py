n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

'''
1, 2 win 이면              2,1 win
1, 3 lose 이고,            2,3 lose
2,3 win 이고,              1,3 win
3,1 win 이다.              3,2 win
'''
point1, point2 = 0,0
# 1,2 일때 win이면
for i in range(n):
    p1, p2 = arr[i]
    if p1 == 1 and p2 == 2:
        point1 += 1
    elif p1 == 2 and p2 == 3:
        point1 += 1
    elif p1 == 3 and p2 == 1:
        point1 += 1

# 2,1 일때 win 이면
for i in range(n):
    p1, p2 = arr[i]
    if p1 == 2 and p2 == 1:
        point2 += 1
    elif p1 == 3 and p2 == 2:
        point2 += 1
    elif p1 == 1 and p2 == 3:
        point2 += 1

print(max(point1,point2))