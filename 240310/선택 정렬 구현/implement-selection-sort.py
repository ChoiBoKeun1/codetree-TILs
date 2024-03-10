n = int(input())
arr = list(map(int,input().split()))


for i in range(n-1):
    MIN_IDX = i
    
    for j in range(i+1,n):
        if arr[j] < arr[MIN_IDX]:
            MIN_IDX = j

    arr[i],arr[MIN_IDX] = arr[MIN_IDX],arr[i]

for e in arr:
    print(e, end=' ')