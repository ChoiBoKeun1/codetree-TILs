n,m = map(int,input().split())
arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

ans = 0
for i in range(n-m+1):
    if sorted(arr_A[i:i+m]) == sorted(arr_B):
        ans += 1

print(ans)