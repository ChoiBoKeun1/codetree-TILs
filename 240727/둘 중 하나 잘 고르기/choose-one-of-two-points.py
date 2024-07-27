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

# DP 갱신
# 현재 카드 : cards[k]
for k in range(2*n):
    red, blue = cards[k]

    # 역순으로 순회 n ~ 0
    # i : 선택한 빨간 카드의 개수
    # j : 선택한 파란 카드의 개수
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            # 빨간 카드를 선택한 경우
            # 이전거에서 + red
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + red)
            # 파란 카드를 선택한 경우
            # 이전거에서 + blue
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + blue)

# 결과 출력
print(dp[n][n])