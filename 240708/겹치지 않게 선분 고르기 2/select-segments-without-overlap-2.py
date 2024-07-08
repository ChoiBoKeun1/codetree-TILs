n = int(input())
lines = list()

for _ in range(n):
    x1, x2 = map(int,input().split())
    lines.append((x1,x2))

# 끝점을 기준으로 오름차순 정렬
lines.sort(key=lambda x: x[1])

# dp[i]: i번째 선분까지 고려했을 때 겹치지 않게 선택할 수 있는 선분의 최대 수
# 초기값 : 1. 최소한 각 선분 자체를 선택할수 있기 때문
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # j번째 선분이 i번째 선분보다 앞에 있다.
        # --> j번째 선분 끝점이 i번째 선분 시작점보다 작다.
        if lines[j][1] < lines[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))