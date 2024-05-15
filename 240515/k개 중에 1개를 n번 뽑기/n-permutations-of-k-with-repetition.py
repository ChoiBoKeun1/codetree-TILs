k,n = map(int,input().split())

arr = []

def Print():
    for elem in arr:
        print(elem, end=' ')
    print()

def choose(cur_idx):
    if cur_idx == n:
        Print()
        return

    else:
        for i in range(1,k+1):
            arr.append(i)
            choose(cur_idx +1)
            arr.pop()

choose(0)