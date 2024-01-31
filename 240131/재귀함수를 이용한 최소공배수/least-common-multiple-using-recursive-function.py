n = int(input())
arr = list(map(int,input().split()))

    

mul = 1
for i in arr:
    if mul % i != 0:
        mul *= i

print(mul)