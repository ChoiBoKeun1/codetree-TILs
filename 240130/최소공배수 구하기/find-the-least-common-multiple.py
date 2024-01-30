n,m = map(int,input().split())

if n > m: 
    n,m = m,n

mul = n * m

while m != 0:
    tmp = n % m
    n = m
    m = tmp

# n 은 최대공약수

print(int(mul / n))