x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    digit = [0] * 10
    total_digit = len(str(i))
    for s in str(i):
        digit[int(s)] += 1

    interesting = False

    for j in range(10):
        if digit[j] == total_digit-1:
            interesting = True

    if interesting:
        ans += 1

print(ans)