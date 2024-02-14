n,b = map(int,input().split())
arr = [
    int(input())
    for _ in range(n)
]

arr.sort()
ans = 0
for i in range(n):
    cnt = 0
    total_price = arr[i] // 2
    
    if total_price <= b:
        cnt += 1

        for j in range(n):
            if i == j:
                continue
            
            total_price += arr[j]
            
            if total_price > b:
                break

            cnt += 1
        
        ans = max(ans,cnt)
    

print(ans)