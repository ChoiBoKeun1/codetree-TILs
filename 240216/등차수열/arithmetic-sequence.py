n = int(input())
arr = list(map(int,input().split()))

# k 찾기
ans = 0
for k in range(1,101):
    # arr 에서 숫자 두개를 가져와서
    for i in range(n):
        for j in range(i+1,n):
            if i == j:
                continue
            if arr[j] - k == k - arr[i]:
                ans += 1
print(ans)