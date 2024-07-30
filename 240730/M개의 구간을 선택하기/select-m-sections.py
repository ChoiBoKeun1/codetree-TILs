N, M = map(int, input().split())
nums = list(map(int, input().split()))

# Initialize DP table
MIN_VAL = float('-inf')
dp = [[[MIN_VAL] * 2 for _ in range(M + 1)] for _ in range(N + 1)]

# Base case
for i in range(N + 1):
    dp[i][0][0] = 0  # If no intervals are selected, the maximum sum is 0.

# Fill DP table
for i in range(1, N + 1):
    for j in range(1, M + 1):
        # When the i-th element is not included in the current interval
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
        
        # When the i-th element is included in the current interval
        if j > 1:
            dp[i][j][1] = max(dp[i-1][j-1][0] + nums[i-1], dp[i-1][j][1] + nums[i-1])
        else:
            dp[i][j][1] = dp[i-1][j-1][0] + nums[i-1]

# Find the maximum value for M intervals
result = max(dp[N][M][0], dp[N][M][1])

# Output the result
print(result)