n = int(input())
arr = list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        if i == j or abs(i-j) == 1:
            continue
        ans = max(ans, arr[i]+arr[j])

print(ans)