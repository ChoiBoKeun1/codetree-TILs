x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    n = str(i)
    rev_n = ''.join(reversed(n))
    
    if n == rev_n:
        ans += 1

print(ans)