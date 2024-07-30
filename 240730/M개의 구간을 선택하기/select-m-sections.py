n,m = map(int,input().split())
nums = list(map(int,input().split()))

# dp[i][j][k]
# i는 현재 위치, j는 선택한 구간의 수, k는 현재 구간이 진행 중인지 여부(0 or 1)
dp = [
    [
        [-1 for _ in range(2)]
        for _ in range(m+1)
    ]
    for _ in range(n+1)
]
dp[0][0][0] = 0

for i in range(1, n+1):
    for j in range(0, m+1):
        # 현재 구간이 진행 중이지 않은 경우
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])

        if j > 0 and i > 1:
            # 현재 구간이 진행 중인 경우
            dp[i][j][1] = max(dp[i][j][1], dp[i-2][j-1][0] + nums[i-1])
            dp[i][j][1] = max(dp[i][j][1], dp[i-2][j-1][1] + nums[i-1])
        
        if i > 1:
            # 현재 구간이 계속 진행 중인 경우
            dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][1] + nums[i-1])


print(max(dp[n][m]))