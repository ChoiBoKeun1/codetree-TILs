k,n = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(k)
]

ans = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue

        isAns = True

        for a in arr:
            if a.index(i) >= a.index(j):
                isAns = False
        
        if isAns:
            ans += 1

print(ans)