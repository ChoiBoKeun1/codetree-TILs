n = int(input())
arr = list(map(int,input().split()))

def get_average(i,j):
    sum_val = 0
    average = 0

    for k in range(i,j+1):
        sum_val += arr[k]

    average = sum_val / (j-i)

    if average.is_integer():
        average = int(average)
    
    return average


ans = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            ans += 1
            continue

        average = get_average(i,j)
        
        if average in arr[i:j+1]:
            ans += 1

print(ans)