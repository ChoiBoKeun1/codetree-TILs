import sys
INT_MAX = sys.maxsize

n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

permutation = [0]
visited = [False] * (n)
visited[0] = True

ans = INT_MAX

def calc():
    result = 0

    permutation.append(0)
    for i in range(n):
        val = arr[permutation[i]][permutation[i+1]]
        
        if val == 0:
            permutation.pop()
            return INT_MAX
        
        result += val
    
    permutation.pop()
    return result

def make_p(cnt):
    global ans

    if cnt == n:
        ans = min(ans, calc())
        return

    for i in range(1,n):
        if visited[i]:
            continue

        permutation.append(i)
        visited[i] = True

        make_p(cnt+1)

        permutation.pop()
        visited[i] = False

make_p(1)
print(ans)