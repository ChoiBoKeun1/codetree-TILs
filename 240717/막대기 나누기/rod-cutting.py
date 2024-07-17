n = int(input())
prices = [0] + list(map(int,input().split()))

# dp[i] : 길이 i 인 막대를 잘라 얻을수 있는 최대 수익
dp = [0] * (n+1)

# 길이 1 ~ n 까지 각 길이에 대해 최대 수익을 계산
for i in range(1, n+1):
    # 각 길이 i 에 대해, 
    # 가능한 모든 자르는 길이 j 를 고려. (1 ~ i)
    for j in range(1, i+1):
        dp[i] = max(dp[i], prices[j] + dp[i-j])
        # 길이가 i인 막대를 이용해 얻을 수 있는 수익 (dp[i])
        # = 길이가 j인 막대를 팔았을때의 수익(prices[j]) 
        # + 나머지 길이 (i-j)인 막대를 이용해 얻을 수 있는 수익(dp[i-j])

print(dp[n])