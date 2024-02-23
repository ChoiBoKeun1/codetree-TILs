a,b,x,y = map(int,input().split())

ans = 101

# 순간이동 안써도 될경우
ans = min(ans, abs(b-a))

# 순간이동을 쓸 경우
# a -> x -> y -> b
ans = min(ans,abs(a-x) + abs(y-b))

# a -> y -> x -> b
ans = min(ans,abs(a-y) + abs(x-b))

print(ans)