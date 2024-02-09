MAX_NUM = 100

n,k = map(int,input().split())
arr = [0] * (MAX_NUM+1)

for _ in range(n):
    num, idx = map(int,input().split())
    arr[idx] += num

ans = 0
# i는 시작점 idx
for i in range(MAX_NUM):
    sum_val = 0
    
    for j in range(i-k, i+k+1):
        if j >= 0 and j <= MAX_NUM:
            sum_val += arr[j]

    ans = max(ans,sum_val)

print(ans)