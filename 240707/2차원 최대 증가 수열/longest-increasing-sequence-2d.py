n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
# -1 : 방문하지 않았음을 의미
dp = [
    [-1] * m
    for _ in range(n)
]

def dfs(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 1

    for i in range(x + 1, n):
        for j in range(y + 1, m):
            if arr[i][j] > arr[x][y]:  # 점프한 곳의 값이 더 큰 경우
                dp[x][y] = max(dp[x][y], dfs(i, j) +1)
    
    return dp[x][y]

print(dfs(0,0))