n,m = map(int,input().split())

# adjacency matrix
graph = [
    [0] * (n+1)
    for _ in range(n+1)
]

visited = [False] * (n+1)
ans = 0

def dfs(v):
    global ans

    for cur_v in range(1, n+1):
        if graph[v][cur_v] and not visited[cur_v]:
            ans += 1
            visited[cur_v] = True
            dfs(cur_v)

# 간선 표현
for _ in range(m):
    v1, v2 = map(int,input().split())
    
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# main
visited[1] = True
dfs(1)
print(ans)

'''
# adjacency list
graph = [
    []
    for _ in range(n+1)
]
visited = [False] * (n+1)
ans = 0

def dfs(v):
    global ans

    for cur_v in graph[v]:
        if not visited[cur_v]:
            visited[cur_v] = True
            ans += 1
            dfs(cur_v)

# 간선 표현
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(ans)
'''