a1, a2 = map(int,input().split())

def func(n :int):
    if n == 1:
        return a1
    elif n == 2:
        return a2     
    else:
        return func(n-1) + 2 * func(n-2)

for i in range(1,11):
    print(func(i),end=' ')