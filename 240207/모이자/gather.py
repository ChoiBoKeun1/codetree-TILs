import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int,input().split()))

ans = INT_MAX

# i번째 집으로 모이자
for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += arr[j] * abs(i-j)
    ans = min(ans,sum_val)

print(ans)