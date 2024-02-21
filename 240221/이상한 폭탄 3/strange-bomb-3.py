MAX_NUM = 1000000

n,k = map(int,input().split())
arr = [
    int(input())
    for _ in range(n)
]

bomb = [0] * (MAX_NUM+1)
explode = [False] * n


maxval = 0
maxidx = 0
for i in range(n):
    for j in range(i+1,n):
        if j-i > k:
            break
        
        if arr[i] != arr[j]:
            continue

        if not explode[i]:
            explode[i] = True
            bomb[arr[i]] += 1
        
        if not explode[j]:
            explode[j] = True
            bomb[arr[j]] += 1

for i in range(MAX_NUM+1):
    if maxval <= bomb[i]:
        maxval = bomb[i]
        maxidx = i
print(maxidx)