n = int(input())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))

# DP 테이블을 정의합니다. 
# dp[i][j]는 첫 번째 플레이어의 카드에서 i번째까지, 
# 두 번째 플레이어의 카드에서 j번째까지 사용한 상태에서 남우가 얻을 수 있는 최대 점수입니다.
dp = [
    [-1] * (n + 1) 
    for _ in range(n + 1)
]
dp[0][0] = 0

# DP 
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        # 카드 대결 : i번째 첫 번째 플레이어 카드와 j번째 두 번째 플레이어 카드 비교
        if A[i+1] < B[j+1]:
            dp[i+1][j] = max(dp[i][j], dp[i+1][j])

        if A[i+1] > B[j+1]:
            dp[i][j+1] = max(dp[i][j] + B[j+1], dp[i][j+1])
    
        # 카드 버리기
        dp[i+1][j+1] = max(dp[i][j], dp[i+1][j+1])

ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])
print(ans)