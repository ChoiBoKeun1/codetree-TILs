n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 0:
        return False
    
    return True

def dfs(x,y):
    dxs = [1,0]
    dys = [0,1]

    for dx, dy in zip(dxs,dys):
        new_x = x + dx
        new_y = y + dy

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x,new_y)

dfs(0,0)
print(int(visited[n-1][m-1]))