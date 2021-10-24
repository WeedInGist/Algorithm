from collections import deque

N = int(input())
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
results = [0] * (N+1)
for i in range(1,N+1):
    a = list(map(int,input().split()))
    results[i] = a[0]
    for j in a[1:-1]:
        graph[i].append(j)
        in_degree[j] += 1

q = deque()
for i in range (1, N+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        results[i] = max(results[i], results[now]+results[i])
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)
print(in_degree)
print(results)