n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]

MAX_NUM = 1000000
boom = [False] * (n)
boom_cnt = [0] * (MAX_NUM+1)

maxval = 1
maxidx = 0

for i in range(n):
    for j in range(i+1, n):
        if j-i > k:
            break
        
        if arr[i] != arr[j]:
            continue

        if not boom[i]:
            boom[i] = True
            boom[j] = True
            boom_cnt[arr[i]] += 1
            boom_cnt[arr[j]] += 1
        else:
            boom[j] = True
            boom_cnt[arr[j]] += 1

blown_bomb = 0
ans = 0
for i in range(n):
    if boom[i]:
        if blown_bomb < boom_cnt[i]:
            blown_bomb = boom_cnt[i]
            ans = i
        if blown_bomb == boom_cnt[i]:
            if ans < i:
                ans = i
print(ans)