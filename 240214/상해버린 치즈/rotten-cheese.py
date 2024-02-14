class Info1:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class Info2:
    def __init__(self, p, t):
        self.p, self.t = p, t

n, m, d, s = tuple(map(int, input().split()))

info1 = []
for _ in range(d):
    p, x, t = tuple(map(int, input().split()))
    info1.append(Info1(p, x, t))

info2 = []
for _ in range(s):
    p, t = tuple(map(int, input().split()))
    info2.append(Info2(p, t))

ans = 0
# i번째 치즈가 상했다고 가정
for i in range(1, m+1):
    # 각 사람별로, i번째 치즈를 언제 먹었는가를 체크
    # time의 idx = 사람번호
    time = [0] * (n+1)
    for info in info1:
        if info.m != i:
            continue
        person = info.p
        # 이 치즈를 처음 먹은 경우
        if time[person] == 0:
            time[person] = info.t
        # 이 치즈를 가장 처음 먹은 시간을 저장
        elif time[person] > info.t:
            time[person] = info.t
    
    possible = True

    # i번째 치즈를 먹지 않았거나
    # i번째 치즈를 먹기 전에 이미 아프다면
    # i번째 치즈는 상하지 않았다.
    for info in info2:
        person = info.p
        # i번째 치즈를 먹지 않은 경우
        if time[person] == 0:
            possible = False
        # i번째 치즈를 먹기 전에 이미 아픔
        if time[person] >= info.t:
            possible = False

    pill = 0
    if possible:
        # 한번이라도 i번째 치즈를 먹었다면, j번째 사람에게 약을 먹여야 한다.
        for j in range(1,n+1):
            if time[j] != 0:
                pill += 1
    ans = max(ans,pill)

print(ans)