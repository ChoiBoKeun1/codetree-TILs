n = int(input())

white = 0
black = 0

cur_dirc = ""

for _ in range(n):
    num, dirc = map(str, input().split())
    num = int(num)
    if cur_dirc == 'L':
        if dirc == 'L':
            if black == 1:
                white += 1
            white += (num-1)
            cur_dirc = 'L'
        elif dirc == 'R':
            if white > num:
                white -= num
            else:
                white = 0
            black += num
            cur_dirc = 'R'
   
   
    elif cur_dirc == 'R':
        if dirc == 'L':
            if black > num:
                black -= num
            else:
                black = 0
            white += num
            cur_dirc = 'L'
        elif dirc == 'R':
            if white == 1:
                black += 1
            black += (num-1)
            cur_dirc = 'R'
    else:
        if dirc == 'L':
            white += num
            cur_dirc = 'L'
        elif dirc == 'R':
            black += num
            cur_dirc = 'R'

print(white, black)