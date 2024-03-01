n = int(input())
arr = list(map(int,input().split()))

arr.sort()

# 가장 큰 수 3개의 곱이 최대인 경우
# 1. 양 * 양 * 양 -> 가장 큰 수들의 곱
# 2. 음 * 음 * 음 -> 이거 역시 가장 큰수들의 곱
ans1 = arr[-1] * arr[-2] * arr[-3]

# 가장 작은 수 2개 + 가장 큰 수 1개
# 세 수 +-- 의 경우.
ans2 = arr[0] * arr[1] * arr[-1]

# 위의 두 경우 모두 0은 고려 안해도 된다. 어차피 알아서 걸러진다

# 둘 중 큰거
ans = max(ans1,ans2)
print(ans)