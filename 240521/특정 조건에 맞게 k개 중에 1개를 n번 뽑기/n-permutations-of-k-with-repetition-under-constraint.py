k,n = map(int,input().split())

arr = []

def choose(cnt):
    if cnt == n:
        for elem in arr:
            print(elem, end=' ')
        print()
        return

    for i in range(1, k+1):
        if cnt >= 2 and arr[-1] == arr[-2] == i:
            continue
            
        arr.append(i)
        choose(cnt +1)
        arr.pop()

choose(0)