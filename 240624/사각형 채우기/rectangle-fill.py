MAX_N = 1000
MOD = 10007

n = int(input())

# dp[i] : 2 * i 크기의 사각형을 만드는 방법의 수
dp = [0] * (MAX_N +1)

# dp[0] = 1. 사각형을 배치하지 않는 경우 1가지.
# dp[1] = 1. 2 * 1 사각형 하나 배치하는 경우 1가지.
dp[0] = dp[1] = 1

# dp[i] = dp[i-1] + dp[i-2]
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])