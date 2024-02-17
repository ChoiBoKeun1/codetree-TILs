a,b,c = map(int,input().split())

ans = 0
for i in range(c//a + 1):    
    cnt = a*i
    
    num_b = (c-cnt) // b

    cnt += num_b * b
        
    ans = max(ans,cnt)

print(ans)