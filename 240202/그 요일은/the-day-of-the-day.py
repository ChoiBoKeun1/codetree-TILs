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

if days < 0:
    print(0)
else:
    cnt = days // 7
    remainder = days % 7
    if remainder > diff:
        cnt += 1
    print(cnt)

'''
m1,d1,m2,d2 = map(int,input().split())
A = input()

# 1월 1일부터 m월 d일까지 일수
def num_of_days(m,d):
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    total_days = 0

    for i in range(1,m):
        total_days += days[i]
    
    total_days += d

    return total_days

def num_of_day(s):
    if s == "Mon":
        return 0
    elif s == "Tue": 
        return 1
    elif s == "Wed": 
        return 2
    elif s == "Thu": 
        return 3
    elif s == "Fri": 
        return 4
    elif s == "Sat": 
        return 5
    return 6

ans = 0
start_date = num_of_days(m1,d1)
end_date = num_of_days(m2,d2)
cur_day = num_of_day("Mon")

for date in range(start_date, end_date + 1):
    if cur_day == num_of_day(A):
        ans += 1
    cur_day = (cur_day + 1 ) % 7

print(ans)
'''