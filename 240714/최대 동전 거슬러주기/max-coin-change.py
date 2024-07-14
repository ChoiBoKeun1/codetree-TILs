n,m = map(int,input().split())
coins = list(map(int,input().split()))

# dp[i] : 합이 i 일때, 가능한 경우의 수
dp = [0] * (m+1)

for i in range(1, m+1):
    for j in range(n):
        if i >= coins[j]:
            dp[i] = max(dp[i], dp[i - coins[j]] + 1)

ans = -1 if dp[m] == 0 else dp[m]
print(ans)