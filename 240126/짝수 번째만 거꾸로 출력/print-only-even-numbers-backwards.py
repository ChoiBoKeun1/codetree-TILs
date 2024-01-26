string = input()

answer = []

for i in range(len(string)):
    if i % 2 != 0:
        answer.append(string[i])

for i in range(len(answer)):
    print(answer[len(answer)-1 - i],end='')