n = int(input())
arr = list(map(int,input().split()))

ans = 1000000

# i번째 집으로 모이자
for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += arr[j] * abs(i-j)
    ans = min(ans,sum_val)

print(ans)