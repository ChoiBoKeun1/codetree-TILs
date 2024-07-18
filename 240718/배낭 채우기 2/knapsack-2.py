n,m = map(int,input().split())
items = []
for _ in range(n):
    items.append(tuple(map(int,input().split())))
    
# dp[i] : 무게 i 일때, 최대 value
dp = [0] * (m+1)

# 각 보석에 대해
for weight, value in items:
    # 현재 보석을 선택하는 경우
    # dp를 앞에서부터 갱신.
    # dp[i]를 갱신할 때, dp[i - weight]를 참조하는데, 
    # 이미 갱신된 값을 참조하기 때문에 보석의 중복 선택이 가능
    for i in range(weight, m + 1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[m])