import sys

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x1,y1 = arr[i]
        x2,y2 = arr[j]

        dist = (x1-x2)**2 + (y1-y2)**2
        ans = min(ans,dist)
print(ans)