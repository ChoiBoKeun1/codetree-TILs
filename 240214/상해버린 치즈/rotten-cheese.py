n,m,d,s = map(int,input().split())
eat = [
    tuple(map(int,input().split()))
    for _ in range(d)
]
sick = [
    tuple(map(int,input().split()))
    for _ in range(s)
]

sick_people = []

def getSickTime(i):
    sick_time = 0
    for p,t in sick:
        if p == i:
            sick_time = t
    return sick_time

def getPossibleCheezes(i, sick_time):
    possible_cheezes = []
    if sick_time:
        for p,m,t in eat:
            if p == i:
                if t < sick_time:
                    possible_cheezes.append(m)
    return possible_cheezes

for i in range(1, n+1):
    # i번째 사람 기준으로
    # 아팠다고 했는지 확인
    sick_time = getSickTime(i)
    if sick_time and i not in sick_people:
        sick_people.append(i)

    possible_cheezes = getPossibleCheezes(i,sick_time)

    for j in range(1, n+1):
        if i == j:
            continue

        for pos_cheeze in possible_cheezes:
            for p,m,t in eat:
                if m == pos_cheeze and p not in sick_people:
                    sick_people.append(p)

print(len(sick_people))