import sys

# 입력
n, m = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(n)]

# 경험치와 수행시간 리스트 생성
exp = [0] * (n + 1)
runtime = [0] * (n + 1)
for i in range(1, n + 1):
    exp[i], runtime[i] = quests[i-1]

# 최대 수행시간 계산
t = sum(runtime)

# dp 배열 초기화
# dp[i][j] : i번째 퀘스트까지 고려했을때, 총 시간이 j 일때
# 얻을수 있는 최대 경험치.
dp = [
    [-sys.maxsize] * (t + 1) 
    for _ in range(n+1)
]
# 0번째 퀘스트 까지 고려했을때 총 시간은 0 이다.
# 얻을수 있는 경험치도 0 이다.
dp[0][0] = 0

# dp 배열 갱신
for i in range(1, n + 1):
    for j in range(t + 1):
        # Case 1. 현재 퀘스트를 진행하여 
        #         수행시간의 총 합이 j가 되기 위해서는
        #         i - 1번째 퀘스트 까지 수행시간이 j - runtime[i]가 되어야 한다.
        if j - runtime[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j - runtime[i]] + exp[i])

        # Case 2. 현재 퀘스트를 진행하지 않고 
        #         수행시간의 총 합이 j가 되기 위해서는
        #         i - 1번째 퀘스트 까지 수행시간이 j가 되어야 한다.
        dp[i][j] = max(dp[i][j], dp[i-1][j])

# n개의 퀘스트까지 고려했을 때 
# 최대 경험치 합이 m 이상인 경우 중 
# 최소 시간을 계산.
ans = sys.maxsize
for j in range(t + 1):
    if dp[n][j] >= m:
        ans = min(ans, j)

# 불가능하다면 -1
if ans == sys.maxsize:
    ans = -1

print(ans)