n = int(input())
arr = list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        sum_val = 0
        for k in range(i,j):
            sum_val += arr[k]
        sum_val //= (j-i)
        if sum_val in arr[i:j]:
            ans += 1
print(ans)