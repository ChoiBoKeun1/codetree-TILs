n = int(input())

cnt = 0

mylist = list(map(int,input().split()))

for i in range(len(mylist)):
    if mylist[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i+1,end='')
            break