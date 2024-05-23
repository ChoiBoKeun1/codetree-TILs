n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
direction = [
    list(map(int,input().split()))
    for _ in range(n)
]
r,c = map(int,input().split())
r,c = r-1,c-1

ans = 0

# 방향 1~8 사용
dxs = [99,-1,-1,0,1,1,1,0,-1]
dys = [99,0,1,1,1,0,-1,-1,-1]


def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y,num):
    return in_range(x,y) and arr[x][y] > num

def move(x,y,cnt):
    global ans

    ans = max(ans, cnt)
    
    cur_dir = direction[x][y]

    for i in range(1, n+1):
        nx = x + dxs[cur_dir] * i
        ny = y + dys[cur_dir] * i

        if can_go(nx,ny, arr[x][y]):
            move(nx,ny,cnt+1)
            
move(r,c,0)
print(ans)