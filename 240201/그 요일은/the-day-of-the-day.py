m1,d1,m2,d2 = map(int,input().split())
day = input()

day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
_31days = [1,3,5,7,8,10,12]
_30days = [4,6,9,11]
_29days = [2]

def check(month):
    days = 0
    if month in _31days:
        days += 31
    elif month in _30days:
        days += 30
    else:
        days += 29
    return days

# m1 다음월 ~ m2 전월까지의 일수 합
days = 0
for i in range(m1 + 1, m2):
    days += check(i)

# m1월 d1일 ~ m1월 마지막일 까지 days
days += (check(m1) - d1 + 1)

# m2월 일수
days += d2

# m1월 d1일 => 월요일
if day in day_of_week:
    diff = day_of_week.index(day)

days -= diff

cnt = days // 7
remainder = days % 7

print(cnt+1)