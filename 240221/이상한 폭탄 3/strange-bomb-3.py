n,K = map(int,input().split())
arr = [int(input()) for _ in range(n)]

MAX_NUM = 1000000
boom = [0] * (MAX_NUM+1)


for j in range(n):
    for k in range(j+1,n):
        if j == k:
            continue

        if arr[j] == arr[k] and abs(j-k) <= K:
            if not boom[arr[j]]:
                boom[arr[j]] += 1
            boom[arr[j]] += 1

MAX_BOOM = 0
ans = -1
for i in range(MAX_NUM+1):
    if MAX_BOOM < boom[i]:
        MAX_BOOM = boom[i]
        ans = i
    elif MAX_BOOM == boom[i]:
        if ans < i:
            MAX_BOOM = boom[i]
            ans = i
print(ans)