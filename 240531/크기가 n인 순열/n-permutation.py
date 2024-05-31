n = int(input())

visited = [False] * (n+1)
answer = []

def choose(cur_idx):
    if cur_idx == n+1:
        for elem in answer:
            print(elem, end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)

        choose(cur_idx +1)

        answer.pop()
        visited[i] = False

choose(1)