n,m = map(int,input().split())
arr = [0] + list(map(int,input().split()))


def move(i):
    sum_elem = 0
    idx = i
    for j in range(m):
        sum_elem += arr[idx]
        next_idx = arr[idx]
        
        idx = next_idx
    return sum_elem

ans = 0
# i: 시작위치
for i in range(1,n+1):
    cnt = move(i)
    ans = max(ans,cnt)
print(ans)