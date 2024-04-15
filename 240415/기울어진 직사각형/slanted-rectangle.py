n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def get_score(x,y,a,b):
    dxs = [-1,-1,1,1]
    dys = [1,-1,-1,1]

    move_nums = [a,b,a,b]

    sum_val = 0

    # 기울어진 직사각형의 경계를 쭉 따라가기
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x,y = x+dx, y+dy

            # 기울어진 직사각형이 경계를 벗어나는 경우
            # 불가능하다는 의미로, 0을 return.
            if not in_range(x,y):
                return 0
            
            sum_val += arr[x][y]
    
    return sum_val

ans = 0
for i in range(n):
    for j in range(n):
        for a in range(1,n):
            for b in range(1,n):
                ans = max(ans, get_score(i,j,a,b))

print(ans)