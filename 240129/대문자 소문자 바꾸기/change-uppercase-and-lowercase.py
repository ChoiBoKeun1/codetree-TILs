s = input()

for elem in s:
    if elem >= 'a' and elem <= 'z':
        print(elem.upper(), end='')
    else:
        print(elem.lower(), end='')