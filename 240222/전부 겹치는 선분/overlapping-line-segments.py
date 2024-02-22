n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

def intersecting(x1,x2,x3,x4):
    if x2 < x3 or x4 < x1:
        return False
    else:
        return True

possible = True
for i in range(n):
    for j in range(i+1,n):
        if i == j: 
            continue
        x1,x2 = arr[i]
        x3,x4 = arr[j]
        if not intersecting(x1,x2,x3,x4):
            possible = False

if possible:
    print('Yes')
else:
    print('No')