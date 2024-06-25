n = int(input())

MOD = 1000000007

dp = [0] * (1001)
dphalf = [0] * (1001)

# dp[i]. 2*i 사각형을 채우는 방법의 수

# dp[0] = 1. 사각형을 배치하지 않는 경우

# dp[1]. 2*1 사각형을 채우는 방법의 수
# 1*1 2개 or 2*1 1개. dp[1] = 2

dp[1] = 2
dp[2] = 7
dphalf[1] = 1
dphalf[2] = 3
for i in range(3, n+1):
    dp[i] = (dp[i-1]*2 + dp[i-2] + dphalf[i-1] * 2 )  %1000000007
    dphalf[i] = (dp[i-1] + dphalf[i-1]) %1000000007

print(dp[n])