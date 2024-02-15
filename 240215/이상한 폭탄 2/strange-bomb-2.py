n,k = map(int,input().split())
arr = [
    int(input())
    for _ in range(n)
]

ans = -1
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        # 같은 번호 폭탄이 k 거리 안에 있으면 펑
        if arr[i] == arr[j]:
            diff = abs(i-j)
            if diff <= k:
                ans = max(ans,arr[i])

print(ans)