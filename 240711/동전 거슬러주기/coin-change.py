import sys
INT_MAX = sys.maxsize

n,m = map(int,input().split())
coins = list(map(int,input().split()))

# dp[i] : 지금까지 선택한 동전의 합이 i 일때, 가능한 최소 동전의 개수
dp = [INT_MAX] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for j in range(n):
        if i >= coins[j]:
            if dp[i - coins[j]] == INT_MAX:
                continue
            
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)

ans = dp[m]

if ans == INT_MAX:
    ans = -1

print(ans)