n,m = map(int,input().split())
arr = [
    [0] * n
    for _ in range(n)
]

x,y = 0,0
dxs,dys = [1,0,-1,0],[0,1,0,-1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(m):
    r,c = map(int, input().split())
    r,c = r-1,c-1
    arr[c][r] = 1

    adj = 0
    for dx,dy in zip(dxs,dys):
        nx = c + dx
        ny = r + dy
        if in_range(nx,ny) and arr[nx][ny]:
            adj += 1
    
    if adj == 3:
        print(1)
    else:
        print(0)