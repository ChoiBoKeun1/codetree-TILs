n,m = map(int,input().split())
coins = list(map(int,input().split()))

MAX = 10001

# dp[i] : 합이 i 일때, 가능한 최대 동전의 개수
dp = [-1] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for coin in coins:
        if i >= coin and dp[i - coin] != -1:
            dp[i] = max(dp[i], dp[i - coin] + 1)

print(dp[m])