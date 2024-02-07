s = input()
len_s = len(s)
ans = 0

for i in range(len_s - 1):
    for j in range(i + 1, len_s):
        if s[i] == '(' and s[j] == ')':  
            ans += 1

print(ans)