m1,d1,m2,d2 = map(int,input().split())
day = input()

day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_in_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]


days = 0

if m1 != m2:
    # m1 다음월 ~ m2 전월까지의 일수 합
    for i in range(m1 + 1, m2):
        days += days_in_month[i]

    # m1월 d1일 ~ m1월 마지막일 까지 days
    days += (days_in_month[m1] - d1 + 1)

    # m2월 일수
    days += d2
else:
    days += (d2 - d1)
    
# m1월 d1일 => 월요일
if day in day_of_week:
    diff = day_of_week.index(day)

days -= diff

if days < 0:
    print(0)
else:
    cnt = 0
    cnt += days // 7
    print(cnt)