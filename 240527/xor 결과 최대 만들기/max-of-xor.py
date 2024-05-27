n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0

# idx 조합
combination = []

def XOR():
    result = 0
    for elem in combination:
        result ^= arr[elem]

    return result

def choose(start, cnt):
    global ans

    if cnt == m:
        ans = max(ans, XOR())
        return

    for i in range(start, n):
        combination.append(i)
        choose(i+1, cnt+1)
        combination.pop()

choose(0,0)
print(ans)