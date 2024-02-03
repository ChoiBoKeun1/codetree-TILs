n,m,k = map(int,input().split())

# students[1] ~ students[n] n명의 학생
students = [0] * (n + 1)

answer = -1
for i in range(m):
    penalty = int(input())
    students[penalty] += 1
    if answer == -1 and students[penalty] >= k:
        answer = penalty

print(answer)