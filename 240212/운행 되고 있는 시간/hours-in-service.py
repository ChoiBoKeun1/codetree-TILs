n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    # i번째 개발자를 제외한, 나머지 사람들의 근무 시간을 알아보자
    check = [0] * 1001
    total_time = 0

    for j in range(n):
        # i번째 개발자 제외
        if i == j:
            continue
        
        # j번째 개발자의 근무 시간
        a,b = arr[j]

        # j번째 개발자는 a~b-1 까지 일한다를 표시.
        for k in range(a,b):
            check[k] += 1

    # 모든 표시가 끝난 후, '운행되고있는 시간'을 계산
    for elem in check:
        if elem != 0:
            total_time += 1
    ans = max(ans,total_time)

print(ans)