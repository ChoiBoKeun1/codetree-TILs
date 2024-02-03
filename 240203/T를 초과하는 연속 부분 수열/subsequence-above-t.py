n,t = map(int, input().split())
arr = list(map(int,input().split()))

ans,cnt = 0,0
for i in range(n):
    if arr[i] > t:
        if i == 0:
            cnt = 1
        else:
            cnt += 1
    else:
        cnt = 1
    ans = max(ans,cnt)
    print(i, ans)
#print(ans)