import sys

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
ans = sys.maxsize

# i번째 방에서 시작. 0 ~ n-1
for i in range(n):
    dist = 0
    for j in range(i, n+i):
        room = j % n
        if i == room:
            continue
        dist += (j - i) * arr[room]
    ans = min(ans,dist)

print(ans)