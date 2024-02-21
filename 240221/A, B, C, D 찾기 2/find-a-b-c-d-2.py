arr = list(map(int,input().split()))

ans = []

def func():
    for a in range(1,40+1):
        for b in range(1,40+1):
            for c in range(1,40+1):
                for d in range(1,40+1):
                    if all(x in arr for x in (a,b,c,d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d)):
                        ans.append(a)
                        ans.append(b)
                        ans.append(c)
                        ans.append(d)
                        return
func()
for elem in ans:
    print(elem,end=' ')