import sys
INT_MAX = sys.maxsize

n,m = map(int,input().split())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
selected = []
selected2 = []
dist = 0
ans = INT_MAX

def calc():
    x1,y1 = selected2[0]
    x2,y2 = selected2[1]
    return (x1-x2)**2 + (y1-y2)**2

def get_dist(start, cnt):
    global dist

    if cnt == 2:
        dist = 0
        dist = max(dist,calc())
        return

    for i in range(start, m):
        selected2.append(selected[i])
        get_dist(i+1, cnt+1)
        selected2.pop()


def choose(start, cnt):
    global ans, dist

    if cnt == m:
        get_dist(0,0)
        ans = min(ans, dist)
        return

    for i in range(start, n):
        selected.append(points[i])
        choose(i+1, cnt+1)
        selected.pop()
    

choose(0,0)
print(ans)