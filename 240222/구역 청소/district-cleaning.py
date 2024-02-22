a,b = map(int,input().split())
c,d = map(int,input().split())


ans = (b-a) + (d-c)

if b < c or d < a:
    pass
else:
    ans -= min(abs(b-c),abs(d-a))

print(ans)