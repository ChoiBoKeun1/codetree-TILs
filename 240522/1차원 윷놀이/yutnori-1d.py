n,m,k = map(int,input().split())
nums = list(map(int,input().split()))

# 말들의 현재 위치를 표시
# 시작위치 : 1
pieces = [1 for _ in range(k)]

ans = 0

def calc():
    score = 0
    for piece in pieces:
        score += (piece >= m)
    
    return score

def find_max(cnt):
    global ans

    # 밑에서 그냥 넘어간 경우에
    # 즉 find_max(cnt+1) 함수를 거치지 않은 경우에
    # if cnt == n 조건문이 걸리지 않는 경우가 생긴다
    # 그러므로, ans를 업데이트하는 코드는 if문 바깥에 적는다.
    ans = max(ans, calc())

    if cnt == n:
        return

    for i in range(k):
        # i번째 말의 현재 위치가 m보다 크다
        # 이미 m번 칸에 도착했다고 판단하고
        # 이후에 이 i번째 말이 선택될 경우는, 그냥 넘어간다.
        if pieces[i] >= m:
            continue
        
        # i번째 말 nums[cnt]만큼 전진
        pieces[i] += nums[cnt]
        find_max(cnt +1)
        pieces[i] -= nums[cnt]

choose(0)
print(ans)