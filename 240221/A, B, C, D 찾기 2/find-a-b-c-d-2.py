arr = list(map(int,input().split()))

for a in range(1,40+1):
    for b in range(a,40+1):
        for c in range(b,40+1):
            for d in range(c,40+1):
                arr2 = [
                    a,b,c,d,
                    a+b, b+c, c+d, d+a, a+c, b+d,
                    a+b+c, a+b+d, a+c+d, b+c+d,
                    a+b+c+d
                ]
                if sorted(arr) == sorted(arr2):
                    print(a,b,c,d)