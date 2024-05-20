import sys

s = input()
n = 6

# num[0] ~ num[5] : a ~ f를 뜻한다
# num[0] = 1 --> a에 1을 대입하겠다는 뜻
num = [0 for _ in range(n)]

ans = -sys.maxsize

def mapping(idx):
    # ex) s[idx] == 'a' 일때, num[0]값이 return 되도록 한다
    return num[ord(s[idx]) - ord('a')]

def calculate():
    length = len(s)
    value = mapping(0)

    for i in range(2, length, 2):
        if s[i-1] == '+':
            value += mapping(i)
        elif s[i-1] == '-':
            value -= mapping(i)
        else:
            value *= mapping(i)
    
    return value

def find_max(cnt):
    global ans

    if cnt == n:
        ans = max(ans, calculate())
        return

    # a ~ f 까지 순서대로
    # 0 ~ 5 까지 순서대로
    # 1~4 중 하나로 채운다
    for i in range(1,5):
        num[cnt] = i
        find_max(cnt +1)

find_max(0)
print(ans)