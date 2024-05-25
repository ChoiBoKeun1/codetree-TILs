import sys

MIN = sys.maxsize

n = int(input())
arr = list(map(int,input().split()))

cur_idx = 0

min_val = MIN

def move(cnt):
    global cur_idx, min_val

    if cur_idx == n-1:
        min_val = min(min_val, cnt)
        return

    dist = arr[cur_idx]

    for i in range(1,dist):
        if cur_idx + i <= n-1:
            cur_idx += i
            move(cnt + 1)

move(0)
ans = min_val if min_val != MIN else -1
print(ans)