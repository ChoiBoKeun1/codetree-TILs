n = int(input())
arr = [
    [] for _ in range(11)
]

for _ in range(n):
    p, position = map(int,input().split())
    arr[p].append(position)

cnt = 0
for p in arr:
    if len(p) > 1:
        for i in range(len(p)-1):
            if p[i] != p[i+1]:
                cnt += 1

print(cnt)