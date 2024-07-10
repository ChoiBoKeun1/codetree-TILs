n = int(input())
jobs = []

for _ in range(n):
    s,e,p = map(int,input().split())
    jobs.append((s,e,p))

# 초기화
jobs.insert(0, (0, 0, 0))  # 1-based index
dp = [0] * (n+1)
    
# dp 배열 채우기
for i in range(1, n+1):
    # 현재 알바 선택 안 할 경우
    dp[i] = dp[i-1]
    
    # 현재 알바 선택할 경우
    s,e,p = jobs[i]

    # 이진 탐색으로 겹치지 않는 마지막 알바 찾기
    lo, hi = 0, i - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if jobs[mid][1] < s:
            lo = mid
        else:
            hi = mid - 1
            
    if jobs[lo][1] < s:
        dp[i] = max(dp[i], p + dp[lo])

print(dp[n])