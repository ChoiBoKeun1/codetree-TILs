import sys
INT_MIN = -sys.maxsize

n = int(input())
nums = list(map(int,input().split()))

total_sum = sum(nums)

# dp[i][j] : i번째 수까지 고려했을 때 
# 그룹A합 - 그룹B합을 j라 했을 때 
# 가능한 그룹A의 최대 합으로 정의
# j 는 그룹A합 - 그룹B합 이므로, 음수가 될수도 있으니 offset을 사용
dp = [
    [INT_MIN] * (2*total_sum +1)
    for _ in range(n+1)
]
offset = total_sum # offset을 사용하여 음수 인덱스를 방지
dp[0][offset] = 0 # 초기화

for i in range(n):
    for j in range(-total_sum, total_sum + 1):
        if dp[i][j + offset] != INT_MIN:
            # 그룹 A에 nums[i]를 추가하는 경우
            dp[i + 1][j + nums[i] + offset] = max(dp[i + 1][j + nums[i] + offset], dp[i][j + offset] + nums[i])
            # 그룹 B에 nums[i]를 추가하는 경우
            dp[i + 1][j - nums[i] + offset] = max(dp[i + 1][j - nums[i] + offset], dp[i][j + offset])
            # 그룹 C에 nums[i]를 추가하는 경우
            dp[i + 1][j + offset] = max(dp[i + 1][j + offset], dp[i][j + offset])

ans = dp[n][offset] if dp[n][offset] != INT_MIN else 0

print(ans)