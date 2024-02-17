n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    # i번째 점을 지정.
    # 이 점에 x,y축 평행하게 직선 2개를 그린다
    x,y = arr[i]

    remain_points = []
    for x2,y2 in arr:
        if x != x2 and y != y2:
            remain_points.append((x2,y2))
    
    # 이 점들은 모두 한 직선 위에 있어야 한다.
    # 그렇지 않으면 직선 3개로는 불가능하다
    isOnLineX = True
    isOnLineY = True
    length = len(remain_points)

    # 남은 점들 x값 모두 같은지 비교
    # 남은 점들 y값 모두 같은지 비교
    for j in range(length):
        for k in range(length):
            if j==k: 
                continue
            x2,y2 = remain_points[j]
            x3,y3 = remain_points[k]
            if x2 != x3:
                isOnLineX = False
            if y2 != y3:
                isOnLineY = False

    if not isOnLineX and not isOnLineY:
        ans = 0
    else:
        ans = 1
        break

print(ans)