from collections import deque
q = deque()

n = int(input())

MAX = 1000000

visited = [False] * (MAX +1)
ans = 0

def bfs():
    global ans

    q.append((n,0))
    visited[n] = True

    next = 0
    while q:
        now,cnt = q.popleft()

        if now == 1:
            ans = cnt
            return

        next = now +1
        if next <= MAX and not visited[next]:
            q.append((next, cnt +1))
            visited[next] = True

        next = now -1
        if next >= 1 and not visited[next]:
            q.append((next, cnt +1))
            visited[next] = True
        
        if now % 2 == 0:
            next = now // 2
            if not visited[next]:
                q.append((next, cnt +1))
                visited[next] = True

        if now % 3 == 0:
            next = now // 3
            if not visited[next]:
                q.append((next, cnt +1))
                visited[next] = True



bfs()
print(ans)