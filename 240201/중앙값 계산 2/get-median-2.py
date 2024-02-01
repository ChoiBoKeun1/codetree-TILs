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

'''
n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    if i % 2 == 0:
        sorted_arr = sorted(arr[:i+1])
        print(sorted_arr[i//2], end=' ')
'''