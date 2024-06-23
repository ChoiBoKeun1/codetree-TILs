n = int(input())

MAX = 1000
MOD = 10007

dp = [0 for _ in range(MAX+1)]
dp[0] = 1

for i in range(1, n+1):
    if i >= 2:
        dp[i] = (dp[i] + dp[i-2]) % MOD
    if i >= 3:
        dp[i] = (dp[i] + dp[i-3]) % MOD

print(dp[n])