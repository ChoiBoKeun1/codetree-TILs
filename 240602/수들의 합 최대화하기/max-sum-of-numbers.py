n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

permutation = []
visited = [False] * n

ans = 0

def calc():
    val = 0
    for i,j in enumerate(permutation):
        val += arr[i][j]
    
    return val

def make_p(cnt):
    global ans

    if cnt == n:
        ans = max(ans, calc())
        return
    
    for i in range(n):
        if visited[i]:
            continue

        permutation.append(i)
        visited[i] = True

        make_p(cnt+1)

        permutation.pop()
        visited[i] = False

make_p(0)
print(ans)