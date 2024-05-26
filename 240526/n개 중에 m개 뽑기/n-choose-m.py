n,m = map(int, input().split())

answer = []
visited = [False] * 11

def choose(cur_num, cnt):
    global answer, visited

    if cnt == m:
        for i in answer:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i] == False and cur_num < i:
            visited[i] = True
            answer.append(i)
            choose(i, cnt +1)
            answer.pop()
            visited[i] = False

choose(0,0)