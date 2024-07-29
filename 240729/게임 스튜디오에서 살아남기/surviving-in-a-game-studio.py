n = int(input())
MOD = 10**9 + 7

# dp[i][j][k] : i번째 날에
# T를 총합 j회 받았고
# B를 최근 k회 연속 받은 경우의 가짓수
dp = [
    [
        [0 for _ in range(3)]
        for _ in range(3)
    ]
    for _ in range(n+1)
]
dp[0][0][0] = 1

'''
dp[i][j][k] 에 
1. G를 추가하면
    다음날이므로 i+1
    T 개수는 변함이 없으므로 j
    연속된 B가 아니게 되니까 0
    dp[i+1][j][0] += dp[i][j][k]

2. B를 추가하면
    다음날이므로 i+1
    T 개수는 변함이 없으므로 j
    연속된 B 1개 추가 k+1. 단, k < 2 이어야 한다. 
        3 넘어가면 해고이므로(0,1,2 idx) 문제 조건에 위배.
    dp[i+1][j][k+1] += dp[i][j][k] (k < 2)

3. T를 추가하면
    다음날이므로 i+1
    T 1개 추가 j+1. 단 j < 2 이어야 한다.
        3 넘어가면 해고이므로(0,1,2 idx) 문제 조건에 위배.
    연속된 B가 아니게 되니까 0
    dp[i+1][j+1][0] += dp[i][j][k] (j < 2)
'''

for i in range(n): # i 번째 날
    for j in range(3):  # T를 총합 j번 받음
        for k in range(3):  # B를 최근 k회 연속 받음
            # G를 추가
            dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % MOD  
            
            # B를 추가
            if k < 2:
                dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % MOD  
            
            # T를 추가
            if j < 2:
                dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % MOD  

ans = 0
for j in range(3):
    for k in range(3):
        ans = (ans + dp[n][j][k] % MOD)

print(ans)