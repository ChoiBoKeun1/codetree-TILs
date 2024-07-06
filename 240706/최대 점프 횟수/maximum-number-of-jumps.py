import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int,input().split()))

# dp[i] : 점프하여 도착한 마지막 위치를 i라 했을 때, 가능한 최대 점프 횟수
dp = [INT_MIN] * n
dp[0] = 0

for i in range(1,n):
    for j in range(i):
        if dp[j] == INT_MIN:
            continue
        
        if j + arr[j] >= i:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))