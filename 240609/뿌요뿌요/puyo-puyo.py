import sys

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

ans = 0
cur_block_num = 0

cur_size = 0
max_size = 0

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y, color):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False

    if arr[x][y] != color:
        return False

    return True

def dfs(x,y):
    global cur_block_size

    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx,ny, arr[x][y]):
            visited[nx][ny] = True
            cur_block_size += 1
            dfs(nx,ny)
            
# main
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            visited[x][y] = True
            cur_block_size = 1
            
            cur_num = arr[x][y]
            
            dfs(x,y)

            if cur_block_size >= 4:
                ans += 1

            max_size = max(max_size, cur_block_size)

print(ans, max_size)