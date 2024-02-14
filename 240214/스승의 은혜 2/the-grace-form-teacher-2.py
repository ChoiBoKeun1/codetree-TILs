n,b = map(int,input().split())
arr = [
    int(input())
    for _ in range(n)
]

total_price = 0
cnt = 0
arr.sort()

for i in range(n):
    total_price += arr[i] // 2
    cnt += 1
    for j in range(n):
        if i == j:
            continue
        
        total_price += arr[j]
        cnt += 1
        if total_price > b:
            break
    else:
        continue
    break

print(cnt)