n = int(input())
cards = [
    tuple(map(int, input().split())) 
    for _ in range(2*n)
]

# DP 테이블 초기화
dp = [
    [-1] * (n+1) 
    for _ in range(n+1)
]
dp[0][0] = 0

# DP 테이블 갱신
for k in range(2*n):
    red, blue = cards[k]
    for i in range(min(k + 1, n), -1, -1):
        for j in range(min(k + 1, n), -1, -1):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + red)
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + blue)

# 결과 출력
print(dp[n][n])