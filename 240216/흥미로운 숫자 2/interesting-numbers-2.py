x,y = map(int,input().split())

ans = 0
for i in range(x,y+1):
    num = [0] * 10
    for s in str(i):
        num[int(s)] += 1

    zero_cnt = 0
    non_zero_list = []
    for n in num:
        if n == 0:
            zero_cnt += 1
        else:
            non_zero_list.append(n)
    if zero_cnt == 8:
        if non_zero_list[0] == 1 or non_zero_list[1] == 1:
            ans += 1
print(ans)