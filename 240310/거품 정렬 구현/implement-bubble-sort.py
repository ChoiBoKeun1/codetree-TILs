n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

for elem in arr:
    print(elem, end=' ')