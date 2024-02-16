n = int(input())
h = [
    int(input())
    for _ in range(n)
]

ans = 0
# i : 해수면 높이
for i in range(1,1001):
    cnt = 0
    isVisit = [False] * n

    for j in range(n):
        if h[j]-i > 0 and not isVisit[j]:
            isVisit[j] = True
            
            for k in range(j+1, n):
                if j == k:
                    continue
                    
                if h[k]-i > 0:
                    isVisit[k] = True
                else:
                    cnt += 1
                    break
            
        if isVisit[n-1] == True:
            cnt += 1
        ans = max(ans,cnt)
print(ans)