n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

possible = False

for i in range(n):
    max_x1 = 0
    min_x2 = 101
    for j in range(n):
        if i == j:
            continue

        x1,x2 = arr[j]
        max_x1 = max(max_x1,x1)
        min_x2 = min(min_x2,x2)
            
        if max_x1 < min_x2:
            possible = True    
if possible:
    print('Yes')
else:
    print('No')