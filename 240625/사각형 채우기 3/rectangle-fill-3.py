n = int(input())

MOD = 1000000007

dp = [0] * (n+1)

# dp[i]. 2*i 사각형을 채우는 방법의 수

# dp[0] = 1. 사각형을 배치하지 않는 경우

# dp[1]. 2*1 사각형을 채우는 방법의 수
# 1*1 2개 or 2*1 1개. dp[1] = 2

dp[0] = 1
dp[1] = 2

# dp[i] 는
# dp[i-2] 에다가 2*2 사각형을 붙이기 -> 2*2 사각형은 4가지가 있다.
# dp[i-1] 에다가 2*1 사각형을 붙이기 -> 2*1 사각형은 2가지가 있다.
# 1*1 사각형 4개를 붙이는 경우가 위 아래 하나씩 중복되니까 1개를 빼줘야 함.

for i in range(2, n+1):
    dp[i] = (dp[i-2] * 4 + dp[i-1] * 2 - 1) % MOD

print(dp[n])