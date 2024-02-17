a,b,c = map(int,input().split())

ans = 0
for i in range(1000):
    for j in range(1000):
        cnt = a*i + b*j
        if cnt <= c:
            ans = max(ans,cnt)

print(ans)