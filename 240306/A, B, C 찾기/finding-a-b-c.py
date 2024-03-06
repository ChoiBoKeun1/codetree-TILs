arr = list(map(int,input().split()))
arr.sort()
'''
a <= b <= c
1. 2a <= a+b <= c+a
2. a+b <= 2b <= b+c
3. a+c <= b+c <= 2c

1+3.
a+b <= c+a <= b+c

a+b <= c+a <= b+c <= a+b+c

가장 작은 숫자는 a.
그 다음으로 작은 숫자는 b.

그 다음으로 작은 숫자는 c 또는 a+b
'''
a,b,c = arr[0],arr[1],arr[2]
if a+b+c != arr[-1]:
    c = arr[3]

print(a,b,c)