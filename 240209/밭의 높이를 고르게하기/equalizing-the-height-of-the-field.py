import sys

n,h,t = map(int,input().split())
arr = list(map(int,input().split()))

ans = sys.maxsize

for i in range(n):
    for j in range(i+t-1, n):
        # 구간 i ~ j 까지
        cost = 0
        for k in range(i,j+1):
            cost += abs(h - arr[k])
        ans = min(ans,cost)

print(ans)