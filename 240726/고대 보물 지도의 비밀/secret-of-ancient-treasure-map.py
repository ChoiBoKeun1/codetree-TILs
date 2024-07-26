import sys
INT_MIN = -sys.maxsize

n,k = map(int,input().split())
nums = list(map(int,input().split()))

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
    # 현재 숫자가
    # 1. 양수 또는 0
    if nums[i-1] >= 0:
        # 음수의 개수가 j개 일때
        for j in range(k +1):
            dp[i][j] = max(dp[i-1][j] + nums[i-1], nums[i-1])
            ans = max(ans, dp[i][j])
    
    # 2. 음수
    else:
        for j in range(k + 1):
            # 음수를 포함할 수 있을 때의 최대 합을 계산
            if j > 0:
                dp[i][j] = max(dp[i - 1][j - 1] + nums[i - 1], nums[i - 1])
            
            # 음수를 포함할 수 없는 경우의 최대 합을 계산
            else:
                dp[i][j] = nums[i - 1]
            
            ans = max(ans, dp[i][j])

print(ans)