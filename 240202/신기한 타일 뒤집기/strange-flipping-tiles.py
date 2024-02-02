n = int(input())

arr = [0 for _ in range(100000)]

cur_idx = 50000


for _ in range(n):
    white = 0
    black = 0
    num, dirc = map(str, input().split())
    num = int(num)

    if dirc == 'L':
        for i in range(num):
            if cur_idx < 0:
                cur_idx = 99999
            arr[cur_idx] = 1
            if i != num-1:
                cur_idx -= 1

    else:
        for i in range(num):
            if cur_idx > 99999:
                cur_idx = 0
            arr[cur_idx] = 2
            if i != num-1:
                cur_idx += 1
            
for elem in arr:
    if elem == 1:
        white += 1
    elif elem == 2:
        black += 1
print(white, black)