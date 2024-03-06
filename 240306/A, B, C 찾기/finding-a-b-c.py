arr = list(map(int,input().split()))
arr.sort()
'''
a <= b <= c

가장 작은 숫자는 a.
그 다음으로 작은 숫자는 b.
가장 큰 숫자는 a+b+c
'''

a,b = arr[0],arr[1]
c = arr[-1] - (a+b)

print(a,b,c)