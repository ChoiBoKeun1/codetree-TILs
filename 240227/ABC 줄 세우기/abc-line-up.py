n = int(input())
arr = list(input().split())

cnt = 0
for i in range(1,n):
    for j in range(i,0,-1):
        if ord(arr[j-1]) > ord(arr[j]):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            cnt += 1
        else:
            break

print(cnt)