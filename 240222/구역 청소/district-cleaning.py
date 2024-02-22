a,b = map(int,input().split())
c,d = map(int,input().split())

ans = 0
# ab가 cd 보다 앞에 있음
if a <= c:
    # ab와 cd 일부분이 겹치는 경우
    if b >= c:
        ans += (b-a) + (d-c) - (b-c)
    # ab가 cd를 포함하는 경우
    elif b >= d:
        ans += b-a

# cd가 ab 보다 앞에 있음
else:
    # ab와 cd 일부분이 겹치는 경우
    if d >= a:
        ans += (b-a) + (d-c) - (d-a)
    # cd가 ab를 포함하는 경우
    elif d >= b:
        ans += d-c

print(ans)