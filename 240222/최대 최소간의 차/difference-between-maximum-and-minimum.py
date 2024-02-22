import sys

n,k = map(int,input().split())
arr = list(map(int,input().split()))

MAX_NUM = 10000
ans = sys.maxsize
# 최솟값이 i 이라면, 최댓값은 i + k 가 되도록 하자
for i in range(1,MAX_NUM+1):
    total_cost = 0
    for j in range(n):
        cost = 0
        if arr[j] < i:
            cost += abs(arr[j]-i)
        elif arr[j] > i+k:
            cost += abs(arr[j]-i-k)
        total_cost += cost
    ans = min(total_cost, ans)
print(ans)