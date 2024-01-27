string = input()

s1 = string[0]
s2 = string[1]

s = ""

for i in range(len(string)):
    if string[i] == s2:
        s += s1
    else:
        s += string[i]

print(s)