import sys
INT_MIN = -sys.maxsize

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
dp = [
    [INT_MIN] * m
    for _ in range(n)
]
dp[0][0] = 1

# 점프할 지점 (i,j)
for i in range(n):
    for j in range(m):
        # 점프 직전 위치 (x,y)
        for x in range(i):
            for y in range(j):
                # 점프 직전 위치 (x,y) 값이 INT_MIN 이다
                # -> (x,y) 에서 점프하는건 근본적으로 불가능하다
                if dp[x][y] == INT_MIN:
                    continue
                
                # 값이 증가하는 경우에만 갱신
                if arr[x][y] < arr[i][j]:
                    dp[i][j] = max(dp[i][j], dp[x][y] +1)

# 최댓값
ans = INT_MIN
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])
print(ans)