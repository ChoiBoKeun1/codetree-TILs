n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(i,j):
    return i < n and j < m

'''
*   | * * | * * |   * 
* * | *   |   * | * * 
'''
max_sum = 0
for i in range(n):
    for j in range(m):
        if in_range(i+1,j+1):
            tmp_sum = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
            tmp_sum2 = arr[i][j] + arr[i][j+1] + arr[i+1][j]
            tmp_sum3 = arr[i][j] + arr[i][j+1] + arr[i+1][j+1]
            max_sum = max(max_sum, tmp_sum, tmp_sum2, tmp_sum3)
        
        if in_range(i+1,j-1):
            tmp_sum = arr[i][j] + arr[i+1][j] + arr[i+1][j-1]
            max_sum = max(max_sum, tmp_sum)
        
        
'''
* * *  |  *
          *
          *
'''
for i in range(n):
    for j in range(m):
        if in_range(i,j+2):
            tmp_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            max_sum = max(max_sum, tmp_sum)
        if in_range(i+2,j):
            tmp_sum = arr[i][j] + arr[i+1][j] + arr[i+2][j]
            max_sum = max(max_sum, tmp_sum)

print(max_sum)