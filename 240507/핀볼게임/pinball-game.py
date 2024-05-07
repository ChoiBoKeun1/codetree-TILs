n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate(x,y, cur_dir):
    # 상,하,좌,우
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    # / 만나면 : 0<->3 , 1<->2
    # \ 만나면 : 0<->2 , 1<->3

    total_time = 1
    
    while in_range(x,y):
        total_time += 1

        # / 를 만난 경우
        if arr[x][y] == 1:
            cur_dir = 3 - cur_dir
        
        # \ 를 만난 경우
        elif arr[x][y] == 2:
            cur_dir = (cur_dir + 2) % 4

        x = x + dxs[cur_dir]
        y = y + dys[cur_dir]

    return total_time

ans = 0

for i in range(n):
    # 상하좌우 순서. 
    # 상 : 아래에서 위로 올라간다는 뜻

    ans = max(ans, simulate(n-1,i,0))
    ans = max(ans, simulate(0,i,1))
    ans = max(ans, simulate(i,n-1,2))
    ans = max(ans, simulate(i,0,3))

print(ans)