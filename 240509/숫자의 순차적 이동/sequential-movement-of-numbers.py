n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def print_arr(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
    print()

def find_num(cur_num):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == cur_num:
                return (i,j)
    return (-1,-1)

def swap_num(x1,y1, x2,y2):
    arr[x1][y1], arr[x2][y2] = arr[x2][y2],arr[x1][y1]

# arr[x][y] 숫자를 움직인다
def swap(x,y):
    # 아래방향부터. 시계방향으로.
    dxs = [1,1,0,-1,-1,-1,0,1]
    dys = [0,-1,-1,-1,0,1,1,1]

    max_num = 0
    max_x, max_y = x,y

    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx,ny):
            if max_num < arr[nx][ny]:
                max_num = arr[nx][ny]
                max_x,max_y = nx,ny

    swap_num(x,y, max_x,max_y)


for i in range(1, n*n +1):
    x,y = find_num(i)
    swap(x,y)
print_arr(arr)