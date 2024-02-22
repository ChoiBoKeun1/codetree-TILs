n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

# i번째 선분을 제거
for i in range(n):
    max_x1 = 0
    min_x2 = 101
    possible = True

    for j in range(n):
        if i == j:
            continue

        x1,x2 = arr[j]
        max_x1 = max(max_x1,x1)
        min_x2 = min(min_x2,x2)
            
    if min_x2 < max_x1:
        possible = False    

    if possible:
        print('Yes')
        break

if not possible:
    print('No')