n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

num = 0
ans = []

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 0:
        return False
    
    return True

def dfs(x,y):
    global num

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    visited[x][y] = True
    num += 1
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx,ny):
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if can_go(i,j):
            dfs(i,j)
            ans.append(num)
            num = 0

print(len(ans))
for elem in sorted(ans):
    print(elem)