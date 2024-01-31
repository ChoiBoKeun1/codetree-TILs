n,m = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(m):
    sum = 0
    a1,a2 = map(int,input().split())
    for j in range(a1-1,a2):
        sum += arr[j]
    print(sum)