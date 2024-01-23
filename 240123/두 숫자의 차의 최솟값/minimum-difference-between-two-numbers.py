n = int(input())

mylist = list(map(int,input().split()))

minVal = 100

for i in range(n):
    for j in range(i+1,n):
        minVal = min(abs(mylist[i]-mylist[j]),minVal)

print(minVal)