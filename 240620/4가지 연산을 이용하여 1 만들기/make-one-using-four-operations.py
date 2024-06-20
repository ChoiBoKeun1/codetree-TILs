from collections import deque
import sys
import enum

OPERATOR_NUM = 4
INT_MAX = sys.maxsize

class OPERATOR(enum.Enum):
    SUBTRACT = 0
    ADD = 1
    DIV2 = 2
    DIV3 = 3

n = int(input())
ans = INT_MAX

q = deque()
visited = [False for _ in range(2*n)]

# step[i] : n에서 시작하여 i 지점에 도달하기 위한 최단거리
step = [0 for _ in range(2*n)]

# 숫자 num 에 op 연산을 할수 있는가?
def possible(num, op):
    if op == OPERATOR.SUBTRACT.value:
        return True
    elif op == OPERATOR.ADD.value:
        return True
    elif op == OPERATOR.DIV2.value:
        return num % 2 == 0
    else:
        return num % 3 == 0

# 숫자 num 에 op 연산 수행
def calc(num, op):
    if op == OPERATOR.SUBTRACT.value:
        return num -1
    elif op == OPERATOR.ADD.value:
        return num +1
    elif op == OPERATOR.DIV2.value:
        return num // 2
    else:
        return num // 3

def in_range(num):
    return 1 <= num and num <= 2*n - 1

def can_go(num):
    return in_range(num) and not visited[num]

def push(num, new_step):
    q.append(num)
    visited[num] = True
    step[num] = new_step

def bfs():
    global ans

    while q:
        cur_num = q.popleft()

        for i in range(OPERATOR_NUM):
            if not possible(cur_num, i):
                continue

            new_num = calc(cur_num, i)

            if can_go(new_num):
                push(new_num, step[cur_num] + 1)
        
        ans = step[1]

push(n,0)
bfs()
print(ans)