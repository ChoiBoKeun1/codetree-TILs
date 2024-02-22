import sys

n,m,p = map(int,input().split())
message = [
    list(input().split())
    for _ in range(m)
]

# p번째 메세지를 읽지 않은 사람의 수
num_of_unread = int(message[p-1][1])

# p번째 메세지를 읽지 않은 사람이 0명이면, 프로그램 종료
if num_of_unread == 0:
    sys.exit()

# 모든 사람들을 보자
for i in range(n):
    person = chr(ord('A')+i)
    read = False


    for c,u in message:
        u = int(u)
        if u >= num_of_unread and c == person:
            read = True

    if read == False:
        print(person, end=' ')