n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            
            x1,y1 = arr[i]
            x2,y2 = arr[j]
            x3,y3 = arr[k]
            
            if x1 != x2 and x1 != x3 and x2 != x3:
                continue
            if y1 != y2 and y1 != y3 and y2 != y3:
                continue

            area = abs((x1*y2 + x2*y3 + x3*y1)-(x2*y1 + x3*y2 + x1*y3))
            ans = max(area,ans)

print(ans)