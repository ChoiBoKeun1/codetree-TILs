MAX_NUM = 10000

n,k = map(int,input().split())
arr = [0] * (MAX_NUM + 1)

for _ in range(n):
    a,b = map(str,input().split())
    arr[int(a)] = 1 if b == 'G' else 2

ans = 0
for i in range(MAX_NUM - k + 1):
    sum_val = 0
    for j in range(i, i+k+1):
        sum_val += arr[j]
    ans = max(ans, sum_val)

print(ans)