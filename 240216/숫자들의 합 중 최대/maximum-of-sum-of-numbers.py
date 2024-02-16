x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    if i < 10:
       ans = max(ans,i)
    elif i < 100:
        d1,d2 = tuple(map(int,str(i)))
        ans = max(ans, d1+d2)
    elif i < 1000:
        d1,d2,d3 = tuple(map(int,str(i)))
        ans = max(ans, d1+d2+d3)
    elif i < 10000:
        d1,d2,d3,d4 = tuple(map(int,str(i)))
        ans = max(ans, d1+d2+d3+d4)
    else:
        ans = max(ans,1)
print(ans)