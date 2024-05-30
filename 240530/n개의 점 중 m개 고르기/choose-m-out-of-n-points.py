import sys
INT_MAX = sys.maxsize

n,m = map(int,input().split())
points = [
    tuple(map(int,input().split()))
    for _ in range(n)
]
selected = []
ans = INT_MAX

def get_dist():
    x1,y1 = selected[0]
    x2,y2 = selected[1]
    return (x1-x2) ** 2 + (y1-y2) ** 2

def choose(start, cnt):
    global ans

    if cnt == m:
        ans = min(ans, get_dist())
        return

    for i in range(start, n):
        selected.append(points[i])
        choose(i+1, cnt+1)
        selected.pop()
    

choose(0,0)
print(ans)