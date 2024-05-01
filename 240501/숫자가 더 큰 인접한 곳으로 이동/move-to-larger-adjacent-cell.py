n,r,c = map(int,input().split())
r,c = r-1,c-1

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def simulate():
    global r,c

    visited_numbers = []
    flag = True
    # 상하좌우
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]

    max_num = arr[r][c]

    while flag:
        flag = False
        visited_numbers.append(max_num)

        for dx,dy in zip(dxs,dys):
            next_x = r + dx
            next_y = c + dy
            
            if in_range(next_x, next_y):
                if arr[next_x][next_y] > max_num:
                    max_num = arr[next_x][next_y]
                    r,c = next_x,next_y
                    flag = True
                    break
            
    return visited_numbers                


answers = simulate()

for elem in answers:
    print(elem, end=' ')