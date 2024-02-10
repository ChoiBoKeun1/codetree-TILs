n = int(input())
a1,b1,c1 = map(int,input().split())
a2,b2,c2 = map(int,input().split())

def func1(i,j,k):
    if abs(c1-k) % n <= 2 or \
       abs(b1-j) % n <= 2 or \
       abs(a1-i) % n <= 2:
        return True
    return False

def func2(i,j,k):
    if abs(c2-k) % n <= 2 or \
       abs(b2-j) % n <= 2 or \
       abs(a2-i) % n <= 2:
        return True
    return False
    
cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if func1(i,j,k):
                cnt += 1
            if func2(i,j,k):
                cnt += 1
            if func1(i,j,k) and func2(i,j,k):
                cnt -= 1
print(cnt)