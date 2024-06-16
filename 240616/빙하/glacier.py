import collections
q = collections.deque()

n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

num_of_melted = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and not arr[x][y]

def clear_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))

def melt(x,y):
    global arr,visited, num_of_melted

    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    cnt = 0

    for dx,dy in zip(dxs,dys):
        nx,ny = x + dx, y + dy

        if arr[x][y] == 1 and in_range(nx,ny) and visited[nx][ny]:
            arr[x][y] = 0
            num_of_melted += 1
            return

def check():
    return sum(sum(row) for row in arr) > 0

def print_arr(arr):
    for i in range(n):
        for j in range(m):
            print(int(arr[i][j]),end=' ')
        print()
    print()

# main
cnt = 0
while check():
    num_of_melted = 0
    cnt += 1

    visited[0][0] = True
    q.append((0,0))

    bfs()
    #print_arr(visited)
    for i in range(n):
        for j in range(m):
            melt(i,j)
    
    #print_arr(arr)
    clear_visited()

print(cnt, num_of_melted)