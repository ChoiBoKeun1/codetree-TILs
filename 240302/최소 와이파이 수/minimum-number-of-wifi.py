n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans1 = n / (2*m +1)
ans2 = n // (2*m +1)
if ans1 == ans2:
    print(ans2)
else:
    print(ans2 +1)