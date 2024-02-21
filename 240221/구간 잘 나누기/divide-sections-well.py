MAX_ANS = 10000

n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans = MAX_ANS
for i in range(1, MAX_ANS+1):
    # 구간의 합의 최댓값이 i이다.
    
    # possible 구간을 나눌수 있으면 true
    # section 구간 개수
    possible = True
    section = 1

    # 구간 합
    section_sum = 0
    for j in range(n):
        # 어떤 숫자가 '구간 합 최댓값'인 i보다 크다 : 모순
        # 즉시 break. 이번 i는 최댓값이 될 수 없다는 뜻.
        if arr[j] > i:
            possible = False
            break
        
        # j번째 숫자가 들어갔을 때, i 보다 커지면
        # j번째 숫자부터 다음 구간으로 만든다
        if section_sum + arr[j] > i:
            section_sum = 0
            section += 1

        # 이 구간에 j번째 숫자를 집어넣는다.
        section_sum += arr[j]

    # 구간을 나눌 수 있고, 구간의 개수가 m 보다 작거나 같다
    if possible and section <= m:
        ans = min(ans,i)

print(ans)