import sys
INT_MIN = -sys.maxsize

n = int(input())
nums = list(map(int,input().split()))

# dp[i] : 연속부분수열의 마지막 원소의 위치가 i 일때, 얻을수 있는 최대 점수 
dp = [INT_MIN] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))