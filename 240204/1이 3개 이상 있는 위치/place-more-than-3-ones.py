n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 동남서북
dxs, dys = [1,0,-1,0], [0,-1,0,1]

def in_range(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

def check(x,y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt

answer = 0
for i in range(n):
    for j in range(n):
        if check(i,j) >= 3:
            answer += 1

print(answer)