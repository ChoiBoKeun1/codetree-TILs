MAX = 1000000

n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

check = [0] * n


for i in range(n):
    for j in range(i+1, n):
        x11,x12 = arr[i]
        x21,x22 = arr[j]

        # 선분이 겹치려면..
        if x11 <= x21 and x12 >= x22:
            check[i] += 1
            check[j] += 1
        elif x11 >= x21 and x12 <= x22:
            check[i] += 1
            check[j] += 1

ans = 0
for elem in check:
    if elem == 0:
        ans += 1
print(ans)