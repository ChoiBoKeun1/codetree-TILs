n = int(input())

A,B,C = 0,0,0
cur_honor = [1,1,1]

def whoIsFirst():
    honor = [1,1,1]

    if A > B and A > C:
        honor[0],honor[1],honor[2] = 1,0,0
    elif B > A and B > C:
        honor[0],honor[1],honor[2] = 0,1,0
    elif C > A and C > B:
        honor[0],honor[1],honor[2] = 0,0,1
    
    elif A == B and A > C:
        honor[0],honor[1],honor[2] = 1,1,0
    elif A == C and A > B:
        honor[0],honor[1],honor[2] = 1,0,1
    elif B == C and B > A:
        honor[0],honor[1],honor[2] = 0,1,1
    
    elif A == B and B == C:
        honor[0],honor[1],honor[2] = 1,1,1

    return honor

cnt = 0
for _ in range(n):
    c,s = map(str,input().split())
    s = int(s)

    if c == 'A':
        A += s
    elif c == 'B':
        B += s
    else:
        C += s

    new_honor = whoIsFirst()

    if cur_honor != new_honor:
        cnt += 1
        cur_honor = new_honor

print(cnt)