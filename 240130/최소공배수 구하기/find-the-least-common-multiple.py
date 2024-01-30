n,m = map(int,input().split())

def gcd(n,m):
    if n > m: 
        n,m = m,n

    while m != 0:
        tmp = n % m
        n = m
        m = tmp
    
    return n

mul = n * m
gcd = gcd(n,m)

print(int(mul / gcd))