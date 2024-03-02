import sys

n,m = map(int,input().split())
arr = list(map(int,input().split()))
wifi = [False] * n
wifi_range = 2*m + 1

cnt = 0
for i in range(n):
    if arr[i] == 1 and not wifi[i]:
        cnt += 1  
        for j in range(2*m+1):
            if i+j < n:
                wifi[i+j] = True
print(cnt)