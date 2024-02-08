n = int(input())
s = input()

ans = 0
for i in range(n):
    if s[i] != 'C':
        continue
    for j in range(i+1,n):
        if s[j] != 'O':
            continue
        for k in range(j+1,n):
            if s[k] != 'W':
                continue
            ans += 1

print(ans)