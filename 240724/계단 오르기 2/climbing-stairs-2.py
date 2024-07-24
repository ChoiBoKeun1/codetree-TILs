import sys
INT_MIN = -sys.maxsize
MAX_SINGLE_STEP = 3

n = int(input())
coins = list(map(int,input().split()))

dp = [
    [INT_MIN] * (MAX_SINGLE_STEP+1)
    for _ in range(n+1)
]
dp[0][0] = 0

# i는 현재 계단 번호 (1부터 n까지 순회)
for i in range(1, n + 1):
    # j는 한 계단씩 올라간 횟수 (0부터 MAX_SINGLE_STEP까지 순회)
    for j in range(MAX_SINGLE_STEP + 1):
        # 한 계단 올라오기 (단, 한 계단씩 오르는 최대 횟수를 넘지 않아야 함)
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coins[i - 1])
        # 두 계단 올라오기 (단, 현재 계단 번호가 2 이상이어야 함)
        if i >= 2:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coins[i - 1])

print(max(dp[n]))