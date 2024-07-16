n,m = map(int,input().split())
jewels = []


for _ in range(n):
    w,v = map(int,input().split())
    jewels.append((w,v))

jewels.sort()

weight, value = 0,0

for jewel in jewels:
    w,v = jewel

    weight += w
    if weight > m:
        weight -= w
        continue
    value += v

print(value)