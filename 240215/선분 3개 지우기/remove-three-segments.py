n = int(input())
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i == j or j == k or k == i:
                continue

            tmparr = arr[:]
            tmparr.pop(i)
            tmparr.pop(j-1)
            tmparr.pop(k-2)

            check = [0] * 101
            for x1,x2 in tmparr:
                for l in range(x1,x2+1):
                    check[l] += 1
            
            isAns = True
            for ch in check:
                if ch > 1:
                    isAns = False
                    break
            if isAns:
                ans += 1

print(ans)