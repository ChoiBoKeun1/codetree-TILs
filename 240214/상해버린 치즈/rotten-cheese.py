N,M,D,S = map(int,input().split())
eat = [
    tuple(map(int,input().split()))
    for _ in range(D)
]
sick = [
    tuple(map(int,input().split()))
    for _ in range(S)
]

possible_cheezes = []
# i번째 치즈가 상했다고 가정
for i in range(M):
    for p,m,t in eat:
        if m == i:
            for p2,t2 in sick:
                if p == p2 and t < t2 and i not in possible_cheezes:
                    possible_cheezes.append(i)

ans = 0
for possible_cheeze in possible_cheezes:
    cnt = 0
    for p,m,t in eat:
        if m == possible_cheeze:
            cnt += 1
    ans = max(ans,cnt)
print(ans)