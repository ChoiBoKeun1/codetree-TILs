n,m = map(int,input().split())
nums = list(map(int,input().split()))

NUM_MAX = 10001

# dp[i] : 지금까지 선택한 숫자의 합이 i 일때, 가능한 최소 숫자 개수
dp = [NUM_MAX] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if j >= nums[i]:
            dp[j] = min(dp[j], dp[j - nums[i]] + 1)

ans = -1 if dp[m] == NUM_MAX else dp[m]
print(ans)