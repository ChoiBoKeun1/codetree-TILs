import sys

n,m = map(int,input().split())
lines = []
selected_line = []

ans = sys.maxsize

def possible():
    num1 = [i for i in range(n)]
    num2 = [i for i in range(n)]
    
    for i in range(len(lines)):
        _, idx = lines[i]
        num1[idx],num1[idx+1] = num1[idx+1],num1[idx]
    for i in range(len(selected_line)):
        _, idx = selected_line[i]
        num2[idx],num2[idx+1] = num2[idx+1],num2[idx]

    for i in range(n):
        if num1[i] != num2[i]:
            return False

    return True     

def find_min_lines(cnt):
    global ans

    if cnt == m:
        if possible():
            ans = min(ans, len(selected_line))
        return
    
    selected_line.append(lines[cnt])
    find_min_lines(cnt +1)
    selected_line.pop()

    find_min_lines(cnt +1)

for _ in range(m):
    a,b = map(int,input().split())
    lines.append( (b, a-1) )
lines.sort()

find_min_lines(0)
print(ans)