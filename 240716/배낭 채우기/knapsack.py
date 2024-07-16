n,m = map(int,input().split())
items = []
for _ in range(n):
    items.append(tuple(map(int,input().split())))
    
# dp[i] : 무게 i 일때, 최대 value
dp = [0] * (m+1)

# 각 보석에 대해
for weight, value in items:
    # 현재 보석을 선택하는 경우
    # dp를 뒤에서부터 갱신
    for w in range(m, weight -1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[m])