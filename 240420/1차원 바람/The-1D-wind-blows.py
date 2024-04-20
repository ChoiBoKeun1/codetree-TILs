n,m,q = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def print_arr():
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=' ')
        print()

# 행 shift 함수
# 편의를 위해, 'L' : True, 'R' : False 로 설정한다.
def shift(r, d):
    if d == True:
        tmp = arr[r][m-1]
        for i in range(m-1,0,-1):
            arr[r][i] = arr[r][i-1]
        arr[r][0] = tmp
    else:
        tmp = arr[r][0]
        for i in range(m-1):
            arr[r][i] = arr[r][i+1]
        arr[r][m-1] = tmp

# r행 기준으로, 위 아래로 전파
def propagation(r,d, propa_dir):
    # 위쪽으로 전파
    if propa_dir == 'U':
        if r != 0:
            for j in range(m):
                if arr[r][j] == arr[r-1][j]:
                    shift(r-1, ~d)
                    propagation(r-1, ~d, propa_dir)
                    break
    
    # 아래쪽으로 전파
    else:
        if r != n-1:
            for j in range(m):
                if arr[r][j] == arr[r+1][j]:
                    shift(r+1, ~d)
                    propagation(r+1, ~d, propa_dir)
                    break
                    

for _ in range(q):
    r,d = map(str,input().split())
    r = int(r) - 1

    wind_dir = True if d == 'L' else False

    shift(r,wind_dir)
    propagation(r,wind_dir,'U')
    propagation(r,wind_dir,'D')



print_arr()