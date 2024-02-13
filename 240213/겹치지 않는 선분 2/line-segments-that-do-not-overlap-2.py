MAX = 1000000

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    overlap = False

    for j in range(i+1, n):
        x11,x12 = arr[i]
        x21,x22 = arr[j]

        # 선분이 겹치려면..
        if (x11 <= x21 and x12 >= x22) or (x11 >= x21 and x12 <= x22):
            overlap = True
            break
    
    if overlap == False:
        ans += 1

print(ans)