s1 = input()
s2 = input()

n1 = ""
n2 = ""

for s in s1:
    try:
        int(s)
        n1 += s
    except:
        pass

for s in s2:
    try:
        int(s)
        n2 += s
    except:
        pass

print(int(n1)+int(n2))