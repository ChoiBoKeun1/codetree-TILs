import sys
INT_MAX = sys.maxsize
min_val = INT_MAX

n = int(input())
arr = list(map(int,input().split()))

def move(idx, cnt):
    global min_val

    if idx >= n-1:
        min_val = min(min_val, cnt)
        return

    for dist in range(1, arr[idx] + 1):
        move(idx + dist, cnt+1)


move(0,0)
ans = min_val if min_val != INT_MAX else -1
print(ans)