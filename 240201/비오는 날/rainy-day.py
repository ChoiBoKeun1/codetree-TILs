n = int(input())
infos = []

for _ in range(n):
    info = list(map(str,input().split()))
    infos.append(info)

answers = []
for info in infos:
    if info[2] == 'Rain':
        answers.append(info)

answers = sorted(answers)
answer = ' '.join(answers[0])
print(answer)