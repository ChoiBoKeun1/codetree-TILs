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

            isAns = True
            check = [0] * 101
            
            for x in range(n):
                if x == i or x == j or x == k:
                    continue
                x1,x2 = arr[x]
                
                for l in range(x1,x2+1):
                    check[l] += 1                   
            
            for ch in check:
                if ch > 1:
                    isAns = False
                    break
            if isAns:
                ans += 1

print(ans)