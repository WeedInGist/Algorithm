N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
visited = []
for i in range(N):
    visited.append([0 for _ in range(M)])
path = []
length = 999999
def DFS(x,y,path):
    global length
    if x < 0 or x >= M or y < 0 or y >= N:
        return
    if visited[y][x]:
        return
    if graph[y][x] == 0:
        return
    path.append((y,x))
    print(path)
    visited[y][x] = True
    if x == M-1 and y == N-1:
        if length >= len(path):
            length = len(path)
        return
    DFS(x+1,y, path)
    DFS(x,y+1, path)
    DFS(x-1,y, path)
    DFS(x,y-1, path)
DFS(0,0, path)
print(length)