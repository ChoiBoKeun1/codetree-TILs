s = input()
length = len(s)

ans = 0
for i in range(length-4):
    for j in range(i+2,length-1):
        if s[i] == '(' and s[i+1] == '(':
            if s[j] == ')' and s[j+1] == ')':
                ans += 1


print(ans)