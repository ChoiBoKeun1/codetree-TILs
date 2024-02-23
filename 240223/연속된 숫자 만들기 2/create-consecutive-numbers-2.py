arr = list(map(int,input().split()))
arr.sort()

ans = 0

# case 1 : 처음 시작이 연속된 숫자인 경우. 0
if arr[0]+1 == arr[1] and arr[1]+1 == arr[2]:
    ans = 0
# case 2 : 두 숫자만 2만큼 차이나는 경우(앞이든 뒤든)
#   : 멀리 있는 나머지 숫자를 사이에 끼워넣는다. 횟수 = 1
elif arr[0]+2 == arr[1] or arr[1]+2 == arr[2]:
    ans = 1
# case 3 : 모두 떨어져 있는 경우
# 맨앞/맨뒤 숫자를 중간 숫자 +2 위치로 이동.
# 움직이지 않은 맨앞/맨뒤 숫자를 사이에 끼워넣기. 횟수 = 2

else:
    ans = 2
    
print(ans)