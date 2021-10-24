import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, start = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
for i in graph[start]:
    distance[i[0]] = i[1]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i] = cost
                heapq.heappush((q, (cost, i[0])))
count = 0
for i in range(1, N+1):
    if i != start:
        if distance[i] != INF:
            count += 1
for i in range(N+1):
    if distance[i] == INF:
        distance[i] = 0
print(distance)
print(count, max(distance))