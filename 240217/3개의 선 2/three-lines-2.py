n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    # i번째 점을 지정.
    # 이 점에 x,y축 평행하게 직선 2개를 그린다
    x,y = arr[i]

    # 다른 점에 직선을 하나 그어서
    # 모든 점이 지나는지 확인한다.
    isLine = False
    for j in range(n):
        if i == j:
            continue
        x2,y2 = arr[j]
        # j번째 점이 기존 직선을 지나는지 확인
        # 지나면 다음 점을 확인
        if x2 == x or y2 == y:
            continue
        
        # 지나지 않기에, 이 점을 지나는 직선을 그엇다 가정
        # 이제 나머지 점들이 직선 위에 있나 확인하자.
        else: 
            for k in range(n):
                if i == k or j == k:
                    continue
                x3,y3 = arr[k]
                if x3 == x or x3 == x2 or y3 == y or y3 == y2:
                    ans = 1

print(ans)