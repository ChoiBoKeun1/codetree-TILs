n = int(input())

mylist = list(map(int,input().split()))

# 오름차순으로 주어지므로 인접한 두 숫자의 차만 고려하면 된다.

min_val = mylist[1] - mylist[0]

for i in range(2,n):
    if min_val > mylist[i] - mylist[i-1]:
        min_val = mylist[i] - mylist[i-1]

print(min_val)