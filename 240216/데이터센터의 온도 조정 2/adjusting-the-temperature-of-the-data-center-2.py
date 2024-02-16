n,c,g,h = map(int,input().split())

min_t, max_t = 1000, 0
arr = []
for _ in range(n):
    ta,tb = map(int,input().split())
    min_t = min(min_t,ta)
    max_t = max(max_t,tb)
    arr.append((ta,tb))

ans = 0
for i in range(min_t, max_t+1):
    task = 0
    for ta,tb in arr:
        if i < ta:
            task += c
        elif ta <= i and i <= tb:
            task += g
        else:
            task += h
    ans = max(ans,task)

print(ans)