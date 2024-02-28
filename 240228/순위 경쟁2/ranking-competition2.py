n = int(input())

a,b = 0,0

def check():
    if a > b:
        return 'A'
    elif a < b:
        return 'B'
    else:
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