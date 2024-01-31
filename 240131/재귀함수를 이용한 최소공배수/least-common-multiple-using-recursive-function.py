n = int(input())
arr = list(map(int,input().split()))

def gcd(a,b):
    if b == 0:
        return a
    else: 
        return gcd(b, a % b)

def lcm(a,b):
    return int((a * b) / gcd(a,b))

a = arr[0]

for i in range(n-1):
    a = lcm(a,arr[i+1])

print(a)