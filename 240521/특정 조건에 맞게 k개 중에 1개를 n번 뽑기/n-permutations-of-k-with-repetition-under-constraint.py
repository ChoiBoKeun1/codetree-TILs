k,n = map(int,input().split())

arr = []

def choose(cnt):
    if cnt == n:
        for elem in arr:
            print(elem, end=' ')
        print()
        return

    for i in range(1, k+1):
        if arr.count(i) < 2:
            arr.append(i)
            choose(cnt +1)
            arr.pop()

choose(0)