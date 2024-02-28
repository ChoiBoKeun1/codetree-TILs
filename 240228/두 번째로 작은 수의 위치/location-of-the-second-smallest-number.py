import sys

n = int(input())
arr = list(map(int,input().split()))

myarr = sorted(arr)

# 2번째로 작은 숫자가 존재 : True
# low2 : 2번째로 작은 숫자
isexist = False
low2 = 0
for elem in myarr:
    if elem != myarr[0]:
        low2 = elem
        isexist = True
        break

if not isexist:
    print(-1)
    sys.exit()

ansIdx = -1
for i, elem in enumerate(arr):
    if elem == low2:
        if ansIdx != -1:
            print(-1)
            sys.exit()
        
        ansIdx = i

print(ansIdx+1)