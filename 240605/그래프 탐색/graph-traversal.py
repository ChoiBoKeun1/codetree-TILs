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
start_points = []
end_points = []
for i in range(m):
    s,e = map(int,input().split())
    start_points.append(s)
    end_points.append(e)    

for start, end in zip(start_points, end_points):
    graph[start][end] = 1
    graph[end][start] = 1


# main
root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(ans)