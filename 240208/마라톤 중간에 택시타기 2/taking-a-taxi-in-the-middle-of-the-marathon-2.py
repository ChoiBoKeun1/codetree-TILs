import sys
n = int(input())

xs, ys = [],[]
min_dist = sys.maxsize

for _ in range(n):
    x,y = map(int,input().split())
    xs.append(x)
    ys.append(y)

man_dist = 0
# i 번째 체크포인트를 건너뛰자
for i in range(1, n-1):
    new_xs = xs[:i] + xs[i+1:]
    new_ys = ys[:i] + ys[i+1:]

    # 완전 탐색
    for j in range(n-2):    
        man_dist += (abs(new_xs[j] - new_xs[j+1]) + abs(new_ys[j] - new_ys[j+1]))

    min_dist = min(min_dist, man_dist)

print(min_dist)