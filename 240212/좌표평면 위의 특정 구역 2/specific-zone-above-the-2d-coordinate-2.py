import sys

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = sys.maxsize
for i in range(n):
    min_x, min_y = 40001,40001
    max_x, max_y = 0,0
    
    for j in range(n):
        if i == j:
            continue
        
        x,y = arr[j]
        min_x, min_y = min(min_x,x), min(min_y,y)
        max_x, max_y = max(max_x,x), max(max_y,y)
    
    ans = min(ans,(max_y - min_y) * (max_x - min_x))

print(ans)