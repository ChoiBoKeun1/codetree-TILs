import sys

n = int(input())
nums = list(map(int,input().split()))

# 전체 합
total_sum = sum(nums)

# 전체 합이 홀수라면, 절대 sum_A와 sum_B가 같을수 없다.
if total_sum % 2 != 0:
    print('No')
    sys.exit()

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

ans = 'Yes' if dp[target] else 'No'
print(ans)