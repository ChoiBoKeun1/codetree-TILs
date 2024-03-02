import sys

n,m = map(int,input().split())
arr = list(map(int,input().split()))

if m == 0:
    cnt = 0
    for elem in arr:
        if elem == 1:
            cnt += 1
    print(cnt)
    sys.exit()

if not 1 in arr:
    print(0)
    sys.exit()

if m >= n:
    print(1)
    sys.exit()

ans1 = n / (2*m +1)
ans2 = n // (2*m +1)
#print(ans1,ans2)
if ans1 == ans2:
    print(ans2)
elif ans1 < ans2 + 0.5:
    print(ans2)
else:
    print(ans2 +1)