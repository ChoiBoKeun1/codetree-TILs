t,a,b = map(int,input().split())
list_s, list_n = [],[]
for _ in range(t):
    c,x = input().split()
    if c == 'S':
        list_s.append(int(x))
    else:
        list_n.append(int(x))

ans = 0
for i in range(a,b+1):
    d1,d2 = 1000,1000
    for s in list_s:
        d1 = min(d1, abs(i-s))
    for n in list_n:
        d2 = min(d2, abs(i-n))
    if d1 <= d2:
        ans += 1
print(ans)