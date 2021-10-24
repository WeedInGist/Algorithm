N,M = map(int, input().split())
ice_graph = []
for i in range(N):
    ice_graph.append(list(map(int,input())))
fragment = 0
visited = []
start = (0,0)
for i in range(N):
    visited.append([False for _ in range(M)])


def DFS(ice_graph, start, visited):
    if start[0] >= M or start[0] < 0 or start[1] < 0 or start[1] >= N:
        return
    # global fragment
    if visited[start[1]][start[0]]:
        return
    if ice_graph[start[1]][start[0]] == 0:
        visited[start[1]][start[0]] = True
    else:
        return

    DFS(ice_graph, (start[0]+1, start[1]), visited)
    DFS(ice_graph, (start[0]-1, start[1]), visited)
    DFS(ice_graph, (start[0], start[1]+1), visited)
    DFS(ice_graph, (start[0], start[1]-1), visited)
    # fragment += 1

for j in range(N):
    for k in range(M):
        if visited[j][k] == False and ice_graph[j][k] == 0:
            fragment += 1
            DFS(ice_graph, (k, j), visited)
print(fragment)