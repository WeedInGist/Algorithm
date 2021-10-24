visited = [False for _ in range(9)]
graph = [[],
    [0,0,1,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,0],
    [0,1,0,0,1,1,0,0,0],
    [0,0,0,1,0,1,0,0,0],
    [0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,1,0,1],
    [0,1,0,0,0,0,0,1,0]
]

def dfs(graph, v , visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(len(graph[v])):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(graph, i, visited)
print(visited)
dfs(graph, 1, visited)

