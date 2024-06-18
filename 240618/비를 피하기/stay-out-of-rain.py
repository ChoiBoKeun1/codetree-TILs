import collections
import sys
q = collections.deque()
INT_MAX = sys.maxsize

n,h,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
step = [
    [-1 for _ in range(n)]
    for _ in range(n)
]
answer = [
    [INT_MAX for _ in range(n)]
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False

    if visited[x][y] or arr[x][y] == 1:
        return False

    return True

def clear_arr(arr):
    for i in range(n):
        for j in range(n):
            arr[i][j] = 0

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx, ny = x + dx, y + dy

            if can_go(nx,ny):
                step[nx][ny] = step[x][y] + 1
                visited[nx][ny] = True
                q.append((nx,ny))


def people():
    new_list = []

    for i in range(n):
        for j in range(n):
            if len(new_list) == h:
                return new_list
            if arr[i][j] == 2:
                new_list.append((i,j))

    return new_list

def place():
    new_list = []

    for i in range(n):
        for j in range(n):
            if len(new_list) == m:
                return new_list
            if arr[i][j] == 3:
                new_list.append((i,j))
    return new_list

# main
safe_places = place()
for x1,y1 in people():
    #print("사람위치 : ", x1,y1)
    clear_arr(visited)
    clear_arr(step)

    step[x1][y1] = 0
    visited[x1][y1] = True
    q.append((x1,y1))
    
    bfs()

    #print_arr(step)

    for x2,y2 in safe_places:
        #print("안전위치 : ", x2,y2)
        if step[x2][y2] == 0:
            answer[x1][y1] = -1
        elif step[x2][y2] < answer[x1][y1]:
            answer[x1][y1] = step[x2][y2]
        

for i in range(n):
    for j in range(n):
        if answer[i][j] == INT_MAX:
            answer[i][j] = 0

print_arr(answer)