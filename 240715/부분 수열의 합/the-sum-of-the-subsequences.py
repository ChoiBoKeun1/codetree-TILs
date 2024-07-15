n,m = map(int,input().split())
nums = list(map(int,input().split()))

MAX = 10001

# dp[i] : 합이 i일때, 가능한 수
dp = [MAX] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(m, -1, -1):
        if j >= nums[i]:
            dp[j] = min(dp[j], dp[j - nums[i]] + 1)

if dp[m] == MAX:
    print('No')
else:
    print('Yes')