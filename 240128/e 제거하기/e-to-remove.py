s = input()

ans = ""

for i in range(len(s)):
    if s[i] == 'e':
        ans = s[:i] + s[i+1:]
        break

print(ans)