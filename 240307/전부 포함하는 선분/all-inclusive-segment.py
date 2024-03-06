n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 100

for i in range(n):
    min_x1,max_x2 = 101,0
    for j in range(n):
        if i == j:
            continue
        
        x1,x2 = arr[j]
        min_x1 = min(min_x1,x1)
        max_x2 = max(max_x2,x2)
    
    ans = min(ans,max_x2-min_x1)

print(ans)