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

'''
s1 = input()
s2 = input()

n1 = ""
n2 = ""

for s in s1:
    if ord(s) <= ord('9') and ord(s) >= ord('0'):
        n1 += s

for s in s2:
    if ord(s) <= ord('9') and ord(s) >= ord('0'):
        n2 += s

print(int(n1)+int(n2))
'''