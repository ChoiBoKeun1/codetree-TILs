n,m = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def get_num_of_gold(row,col,k):
    return sum([
        arr[i][j]
        for i in range(n)
        for j in range(n)
        if abs(row-i) + abs(col-j) <= k
    ])

ans = 0
max_val = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            numofgold = get_num_of_gold(i,j,k)
            value = numofgold * m
            cost = k*k + (k+1)*(k+1)

            if value - cost > 0 and ans < numofgold:
                ans = numofgold
            

print(ans)