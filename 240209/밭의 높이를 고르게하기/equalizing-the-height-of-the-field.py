import sys

n,h,t = map(int,input().split())
arr = list(map(int,input().split()))

ans = sys.maxsize

# 시작위치 i
# 0 ~ n-t
for i in range(n-t + 1):
    cost = 0

    # 구간 i ~ i+t -1 까지
    for j in range(i, i+t):
        cost += abs(h - arr[j])
    
    ans = min(ans,cost)

print(ans)