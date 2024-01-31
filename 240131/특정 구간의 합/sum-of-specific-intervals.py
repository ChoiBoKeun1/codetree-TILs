n,m = map(int,input().split())
arr = [0] + list(map(int,input().split()))

def func(a1,a2):
    sum = 0
    for i in range(a1,a2+1):
        sum += arr[i]
    return sum

for _ in range(m):
    a1,a2 = map(int,input().split())
    print(func(a1,a2))