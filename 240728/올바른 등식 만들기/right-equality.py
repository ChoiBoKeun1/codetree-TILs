n,m = map(int,input().split())
nums = list(map(int,input().split()))

MAX_SUM = 20
OFFSET = MAX_SUM

# dp[i][j + OFFSET]: i번째 숫자까지 사용하여 합이 j가 되는 방법의 수
dp = [
    [0] * (MAX_SUM * 2 +1)
    for _ in range(n+1)
]
# 초기 상태 설정: 숫자를 하나도 사용하지 않고 합이 0인 경우는 한 가지
dp[0][0 + OFFSET] = 1


for i in range(1, n+1):
    # 현재 숫자
    num = nums[i-1]
    for j in range(-MAX_SUM, MAX_SUM +1):
        # 이전 단계에서 유효한 합이 있는 경우
        if dp[i-1][j + OFFSET] != 0:
            # 더하기 연산
            if -MAX_SUM <= j + num <= MAX_SUM:
                dp[i][j + num + OFFSET] += dp[i-1][j + OFFSET]
            
            # 빼기 연산
            if -MAX_SUM <= j - num <= MAX_SUM:
                dp[i][j - num + OFFSET] += dp[i-1][j + OFFSET]

print(dp[n][m + OFFSET])