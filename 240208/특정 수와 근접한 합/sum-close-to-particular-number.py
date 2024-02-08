import sys

ans = sys.maxsize

n,s = map(int,input().split())
arr = list(map(int,input().split()))

origin_sum_val = sum(arr)

for i in range(n-2):
    for j in range(i+1,n):
        sum_val = origin_sum_val - (arr[i] + arr[j])
        ans = min(ans,abs(s - sum_val))

print(ans)