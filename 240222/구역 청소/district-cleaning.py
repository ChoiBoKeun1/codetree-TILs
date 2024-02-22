a,b = map(int,input().split())
c,d = map(int,input().split())

ans = 0
# ab가 cd 보다 앞에 있음
if a <= c:
    # ab가 cd를 포함하는 경우
    if b >= d:
        ans += b-a
    # ab와 cd 일부분이 겹치는 경우
    elif b >= c:
        ans += (b-a) + (d-c) - (b-c)
    # 안겹치는 경우
    else:
        ans += (b-a) + (d-c)
# cd가 ab 보다 앞에 있음
else:
    # cd가 ab를 포함하는 경우
    if d >= b:
        ans += d-c
    # ab와 cd 일부분이 겹치는 경우
    elif d >= a:
        ans += (b-a) + (d-c) - (d-a)
    else:
        ans = (b-a) + (d-c)
print(ans)