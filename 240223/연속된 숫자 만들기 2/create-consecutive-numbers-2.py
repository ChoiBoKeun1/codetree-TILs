arr = list(map(int,input().split()))
arr.sort()

ans = 0

# case 1 : 처음 시작이 연속된 숫자인 경우. 0
if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
    ans = 0
# case 2 : 앞 두숫자만 붙어있는경우
#   : 맨 앞 숫자를 움직여야 한다 
#   : 맨 뒤 숫자 -2 자리에 둔다. 그럼 맨 앞 숫자를 뒤에 숫자 두개 사이에 끼워넣으면 연속자리. clear +2
elif arr[0]+1 == arr[1]:
    ans = 2
# case 3 : 뒷 두숫자만 붙어있는경우
#   : 맨 뒤 숫자를 움직여야 한다
#   : 맨 앞 숫자 + 2 자리에 둔다. 그럼 맨 뒤 숫자를 앞 숫자 두개 사이에 끼워넣으면 연속자리. clear +2
elif arr[1]+1 == arr[2]:
    ans = 2
# case 4 : 모든 숫자들이 떨어져있는경우
# 맨 앞숫자를 움직일 경우
# 중간 숫자 +2 위치로 이동.
else:
    if arr[1]+2 == arr[2]:
        ans = 1
    else:
        ans = 2
# case4-1: 그 자리가 비어있으면? 그대로 이동
# 1 10 20 -> 10 12 20 -> 10 11 12
# 그 다음 맨 뒤 숫자를 중간에 끼워넣는다. 횟수 = 2
# case4-2: 그 자리가 차있다? 즉
# 1 10 12 인 상황. 중간 숫자 +2 == 맨뒤 숫자인 경우
# 10 11 12 로 이동. 횟수 = 1

print(ans)