MAX_T = 101

n,m = map(int,input().split())
quests = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

# dp[i] : 경험치 i를 얻는데 걸린 시간
dp = [MAX_T] * (m+1)
dp[0] = 0

# 모든 퀘스트를 순회
for e,t in quests:
    # 중복 방지를 위해 역순으로 순회
    for current_exp in range(m, -1, -1):
        next_exp = min(m, current_exp + e)
        dp[next_exp] = min(dp[next_exp], dp[current_exp] + t)

print(dp[m])