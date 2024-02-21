n,l = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
# H점수가 i 일때
# 즉, 수열에 i 이상인 숫자의 수가 i개 이상이라고 가정.
for i in range(1,n+1):
    cnt = 0
    cntl = 0

    # arr의 모든 원소들을 check.
    # 원소들 중 i 이상인 원소들의 개수를 check.
    
    # 원소들 중 값이 정확히 i-1 인 원소들은, 1을 더해주면 i 이상이 된다.
    # 1을 더하기 전에, 지금까지 1을 몇번 더했는지를 check한다(cntl)
    # cntl이 l 보다 작으면, i-1 원소에 1을 더해서 i로 만든다.(cnt += 1)
    for j in range(n):
        if arr[j] >= i:
            cnt += 1
        elif arr[j] == i-1:
            if cntl < l:
                cntl += 1
                cnt += 1

    # 이렇게 센 cnt가 i이상이면 정답이다.
    if cnt >= i:
        ans = i


print(ans)