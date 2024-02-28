n = int(input())

a,b = 0,0

def check():
    # 시작하자마자, a == b 인 경우. 즉 a=0,b=0인 경우. 그냥 넘어간
    if honor == "" and a == b:
        return ""
    
    if a > b:
        return 'A'
    elif a < b:
        return 'B'
    elif a == b:
        return 'AB'

ans = 0
honor = ""
for _ in range(n):
    c,s = tuple(input().split())
    s = int(s)

    if c == 'A':
        a += s
    else:
        b += s

    checking = check()
    
    if honor !=  checking:
        honor = checking
        ans += 1

print(ans)