n = int(input())
prices = list(map(int,input().split()))

# dp[i] : 길이 i 인 막대를 잘라 얻을수 있는 최대 수익
dp = [0] * (n+1)

for i in range(1, n+1):
    max_value = -1
    for j in range(1, i+1):
        max_value = max(max_value, prices[j-1] + dp[i-j])
    dp[i] = max_value

print(dp[n])