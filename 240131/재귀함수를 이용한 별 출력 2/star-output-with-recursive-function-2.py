N = int(input())

def func(n):
    if n == 0:
        return None
    else:
        for _ in range(n):
            print('*',end=' ')
        print()
        func(n-1)

def reverse_func(n):
    if n == N+1:
        return None
    else:
        for _ in range(n):
            print('*',end=' ')
        print()
        reverse_func(n+1)

func(N)
reverse_func(1)