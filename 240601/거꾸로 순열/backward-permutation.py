n = int(input())

arr = list()
visited = [False] * (n+1)

def Print():
    for elem in arr:
        print(elem, end=" ")
    print()

def choose(cnt):
    if cnt == n+1:
        Print()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        arr.append(i)
        visited[i] = True

        choose(cnt+1)
        
        arr.pop()
        visited[i] = False

choose(1)