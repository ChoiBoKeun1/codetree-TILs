mylist = list(map(int,input().split()))

for i in range(len(mylist)):
    if mylist[i] % 3 == 0:
        print(mylist[i-1])
        break