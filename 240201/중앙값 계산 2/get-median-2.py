n = int(input())
arr = list(map(int,input().split()))

def findMid(arr, idx):
    tmpArr = arr[:idx]
    if idx == 1:
        return tmpArr[0]
    else:
        tmpArr.sort()
        return tmpArr[int(idx/2)]
        

for i in range(1,len(arr)+1):
    if i % 2 != 0:
        print(findMid(arr, i), end=' ')