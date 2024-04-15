n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dx = [-1,-1,1,1]
dy = [1,-1,-1,1]

ans = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate(x,y,a,b):
    global ans
    
    sum_val = 0
    is_possible = True

    l = [a,b,a,b]

    for c in range(4):
        if not is_possible:
            break
        
        cur_len = l[c]

        for d in range(cur_len):
            nx = x + dx[c]
            ny = y + dy[c]

            if in_range(nx,ny):
                sum_val += arr[nx][ny]
                x,y = nx,ny

            else:
                is_possible = False
                break

    if is_possible:
        ans = max(ans, sum_val)


for i in range(n):
    for j in range(n):
        for a in range(1,n):
            for b in range(1,n):
                simulate(i,j,a,b)
print(ans)