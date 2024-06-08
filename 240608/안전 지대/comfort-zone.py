n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def clear():
    global visited

    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y, k):
    if not in_range(x,y):
        return False

    if visited[x][y]:
        return False
    
    if arr[x][y] <= k:
        return False

    return True

def dfs(x,y, k):
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    visited[x][y] = True

    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx,ny, k):
            dfs(nx,ny, k)

max_area = 0
ans = 0

# main
for k in range(1, 101):
    num_of_area = 0
    
    for x in range(n):
        for y in range(m):
            if can_go(x,y,k):
                dfs(x,y, k)
                num_of_area += 1

    if num_of_area > max_area:
        max_area = num_of_area
        ans = k
    
    clear()

print(ans, max_area)