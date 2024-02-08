n,k = map(int,input().split())
arr = [""] * (n+1)

for _ in range(n):
    a,b = map(str,input().split())
    arr[int(a)] = b

ans = 0
for i in range(1, n+1 - k + 1):
    sum_val = 0
    for j in range(i, i+k):
        if arr[j] == 'G':
            sum_val += 1
        elif arr[j] == 'H':
            sum_val += 2
    ans = max(ans, sum_val)

print(ans)