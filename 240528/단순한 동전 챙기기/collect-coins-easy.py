import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list()

for i in range(n):
    tmp = input()
    for j in range(n):
        if tmp[j] != '.':
            arr.append((tmp[j],i,j))
arr.sort()

combinations = []
ans = INT_MAX

def make_comb(cur_num, cnt):
    global combinations, ans

    if cur_num > 10:
        return
    
    if cnt == 3:
        dist = simulate()
        ans = min(ans, dist)
        return


    combinations.append(cur_num)
    make_comb(cur_num+1, cnt+1)
    combinations.pop()
    make_comb(cur_num+1, cnt)

def find(num):
    for i in range(len(arr)-2):
        if int(arr[i][0]) == num:
            return (arr[i][1], arr[i][2])
    return (-1,-1)

def simulate():
    global combinations

    dist = 0
    points = list()

    _, start_x, start_y = arr[-1]
    _, end_x, end_y = arr[-2]

    for i in range(len(combinations)):
        x,y = find(combinations[i])
        
        if (x,y) == (-1,-1):
            return INT_MAX

        dist += abs(start_x - x) + abs(start_y - y)
        start_x, start_y = x,y

    dist += abs(start_x - end_x) + abs(start_y - end_y)

    return dist

make_comb(1,0)
if ans == INT_MAX:
    print(-1)
else:
    print(ans)