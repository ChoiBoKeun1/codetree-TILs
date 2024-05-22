n,m,k = map(int,input().split())


dist = list(map(int,input().split()))

# i번 말이 원소값만큼 전진할거임
pieces = [0] * (k+1)

# 선택된 말
selected_pieces = []

# k개의 말, n번의 전진, 각 전진은 dist[] 원소 숫자만큼 전진 가능
# m번(끝)에 도착시 1점을 받는다

ans = 0

def move_all():
    pieces = [0] * (k+1)

    for i in range(n):
        pieces[selected_pieces[i]] += dist[i]

    score = 0
    for elem in pieces:
        if 1 + elem >= m:
            score += 1
    
    return score

def choose(cnt):
    global ans

    if cnt == n:
        score = move_all()
        ans = max(ans, score)
        return

    for i in range(1, k+1):
        selected_pieces.append(i)
        choose(cnt +1)
        selected_pieces.pop()


choose(0)
print(ans)