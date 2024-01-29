s = input()
answer = ""

for elem in s:
    if ord(elem) < 97:
        answer += chr(ord(elem)+26+6)
    else:
        answer += chr(ord(elem)-26-6)
print(answer)