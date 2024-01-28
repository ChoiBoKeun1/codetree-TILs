A = input()
leng = len(A)

cmds = input()

modify_A = ""

for cmd in cmds:
    if cmd == 'L':
        A = A[1:] + A[0] 
    elif cmd == 'R':
        A = A[leng-1] + A[:leng-1]

print(A)