MAX_M = 3
MOD = 10007

n = int(input())

# dp[i] : i를 1,2,5 의 합으로 나타내는 방법의 수
dp = [0] * (n+1)
numbers = [1,2,5]

# 0을 만드는 방법 : 아무것도 더하지 않는 방법 1가지
dp[0] = 1

# dp 갱신
# 외부 for문 i : 현재 목표 합계
# 내부 for문 : 1,2,5 세 숫자 순회
for i in range(1, n+1):
    for j in range(MAX_M):
        if i >= numbers[j]:
            dp[i] = (dp[i] + dp[i-numbers[j]]) % MOD

print(dp[n])