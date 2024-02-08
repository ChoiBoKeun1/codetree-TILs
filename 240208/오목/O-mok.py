n = 19
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def check_col(i,j, num):
    if in_range(i,j+1) and arr[i][j+1] == num and \
       in_range(i,j+2) and arr[i][j+2] == num and \
       in_range(i,j+3) and arr[i][j+3] == num and \
       in_range(i,j+4) and arr[i][j+4] == num:
        return True
    return False

def check_row(i,j, num):
    if in_range(i+1,j) and arr[i+1][j] == num and \
       in_range(i+2,j) and arr[i+2][j] == num and \
       in_range(i+3,j) and arr[i+3][j] == num and \
       in_range(i+4,j) and arr[i+4][j] == num:
        return True
    return False

def check_diagonal(i,j, num):
    if in_range(i+1,j+1) and arr[i+1][j+1] == num and \
       in_range(i+2,j+2) and arr[i+2][j+2] == num and \
       in_range(i+3,j+3) and arr[i+3][j+3] == num and \
       in_range(i+4,j+4) and arr[i+4][j+4] == num:
        return True
    return False

ans = 0
ans_i, ans_j = 0,0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if check_col(i,j,1):
                ans = 1
                ans_i, ans_j = i, j+2
                break
            elif check_row(i,j,1):
                ans = 1
                ans_i, ans_j = i+2, j
                break
            elif check_diagonal(i,j,1):
                ans = 1
                ans_i, ans_j = i+2, j+2
                break
        elif arr[i][j] == 2:
            if check_col(i,j,2):
                ans = 2
                ans_i, ans_j = i, j+2
                break
            elif check_row(i,j,2):
                ans = 2
                ans_i, ans_j = i+2, j
                break
            elif check_diagonal(i,j,2):
                ans = 2
                ans_i, ans_j = i+2, j+2
                break 
    else:
        continue
    break

print(ans)
if ans:
    print(ans_i+1, ans_j+1)