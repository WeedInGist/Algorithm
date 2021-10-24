from collections import deque

visited = [False for _ in range(9)]
graph = [[],
    [0,0,1,1,0,0,0,0,1],
    [0,1,0,0,0,0,0,1,0],
    [0,1,0,0,1,1,0,0,0],
    [0,0,0,1,0,1,0,0,0],
    [0,0,0,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,1,0,1],
    [0,1,0,0,0,0,0,1,0]
]
q = deque([1])
visited[1]=True
def BFS(graph, q, visited):
    while q:
        v = q[0]
        print(v, end=" ")
        q.popleft()
        for i in range(len(graph[1])):
            if graph[v][i] == 1 and visited[i] == False:
                q.append(i)
                visited[i]=True
        print(q)
        BFS(graph, q, visited)
BFS(graph, q, visited)
# print(visited)
