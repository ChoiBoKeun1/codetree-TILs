n,m = map(int,input().split())
arr = [
    tuple(map(int,input().split()))
    for _ in range(m)
]

ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt = 0
        if i == j:
            continue
        
        for a,b in arr:
            if (i == a and j == b) or (i == b and j == a):
                cnt += 1
        ans = max(ans,cnt)
print(ans)