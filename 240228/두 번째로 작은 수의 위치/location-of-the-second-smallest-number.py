n = int(input())
arr = list(map(int,input().split()))

numbers = [0] * 101

for i in range(n):
    numbers[arr[i]] += 1

min_2nd = -1

cnt = 0
for i in range(101):
    if numbers[i] != 0:
        if cnt == 1:
            if numbers[i] == 1: 
                min_2nd = i
            break
        cnt += 1

if min_2nd == -1:
    print(min_2nd)
else:
    for i in range(n):
        if arr[i] == min_2nd:
            print(i+1)
            break