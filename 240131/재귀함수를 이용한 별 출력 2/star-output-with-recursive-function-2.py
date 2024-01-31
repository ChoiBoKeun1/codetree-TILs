n = int(input())

def func(n):
    if n == 0:
        return
    
    for _ in range(n):
        print('*',end=' ')
    print()
        
    func(n-1)

    for _ in range(n):
        print('*',end=' ')
    print()

func(n)