import sys
MIN = sys.maxsize
min_val = MIN

n = int(input())
arr = list(map(int,input().split()))
selected = []

def move(cnt):
    global min_val

    if cnt == n-1:
        min_val = min(min_val, len(selected))
        return

    for i in range(1, arr[cnt]+1):
        if cnt + i <= n-1:
            selected.append(i)
            move(cnt + i)
            selected.pop()


move(0)
ans = min_val if min_val != MIN else -1
print(ans)