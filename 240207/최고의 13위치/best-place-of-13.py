n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    num = 0
    for j in range(n-2):
        num = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        ans = max(ans,num)
print(ans)