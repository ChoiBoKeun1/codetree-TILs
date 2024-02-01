n = int(input())
arr = list(map(int,input().split()))

def findMid(arr, idx):
    if idx == 1:
        return arr[0]
    else:
        arr.sort()
        return arr[int(idx/2)]
        

for i in range(1,len(arr)+1):
    if i % 2 != 0:
        print(findMid(arr, i), end=' ')