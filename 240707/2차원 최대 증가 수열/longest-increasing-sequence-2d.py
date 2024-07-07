n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
dp = [
    [0] * m
    for _ in range(n)
]

dp[0][0] = 1

for i in range(n):
    for j in range(m):
        # 현재 위치가 방문이 가능하다면
        if arr[i][j] != 0:
            for x in range(i+1, n):
                for y in range(j+1, m):
                    # 점프한 곳의 값이 더 큰 경우
                    if arr[x][y] > arr[i][j]:
                        dp[x][y] = max(dp[x][y], dp[i][j]+1)

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans)