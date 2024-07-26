import sys
INT_MIN = -sys.maxsize

n,k = map(int,input().split())
nums = [0] + list(map(int,input().split()))

# dp[i][j] : i번째 숫자까지 고려했을때, 음수의 개수가 j개 일때
# 최대 합
dp = [
    [INT_MIN] * (k+1)
    for _ in range(n+1)
]
dp[0][0] = 0

ans = INT_MIN

# DP
# i는 현재까지 고려한 숫자의 인덱스 (1부터 n까지)
for i in range(1, n +1):
    # 현재 숫자가 양수일 때
    if nums[i] >= 0:
        # 음수 개수는 변하지 않으므로 j를 그대로 유지
        for j in range(k +1):
            dp[i][j] = max(dp[i-1][j] + nums[i], nums[i])
            ans = max(ans, dp[i][j])
    
    # 현재 숫자가 음수일 때
    else:
        # 음수는 1개 ~ k개 까지 나타날수 있다
        for j in range(1, k +1):
            dp[i][j] = max(dp[i-1][j-1] + nums[i], nums[i])
            ans = max(ans, dp[i][j])

print(ans)