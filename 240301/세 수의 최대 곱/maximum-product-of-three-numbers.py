n = int(input())
arr = list(map(int,input().split()))

arr.sort()

# 가장 큰 수 3개
# 세 수 +++ --- 의 곱이 최대인 경우
ans1 = arr[-1] * arr[-2] * arr[-3]

# 가장 작은 수 2개 + 가장 큰 수 1개
# 세 수 +-- 의 경우.
ans2 = arr[0] * arr[1] * arr[-1]

# 둘 중 큰거
ans = max(ans1,ans2)
print(ans)