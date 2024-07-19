n = int(input())
nums = list(map(int,input().split()))

# 전체 합
total_sum = sum(nums)

# 전체 합의 절반. 두 그룹의 합의 차이를 최소화 하기 위해
# 각 그룹의 합이 최대한 절반이 되도록 하기 위해
target = total_sum // 2

# dp[i] : A그룹의 합이 i 가 될수 있는가?
dp = [False] * (target + 1)
dp[0] = True

# 각 숫자에 대해 dp 갱신
for num in nums:
    # [target ~ num] 까지 역순으로 갱신
    for i in range(target, num -1, -1):
        if dp[i - num]:
            dp[i] = True
            # 합이 (i - num) 이 가능하다면, 
            # 거기에 num 을 더하면 i 도 가능하게 됨. 

# 목표값(target) 에 가장 가까운 합을 찾기
# 가장 가까워야 하니까 target 부터 역순으로
# 가장 먼저 나오는 dp[i] == True 인 i 값이 A_sum 이다. 
for i in range(target, -1, -1):
    if dp[i]:
        A_sum = i
        break

B_sum = total_sum - A_sum

print(abs(A_sum - B_sum))