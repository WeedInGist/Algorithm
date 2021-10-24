def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a_1 = find_parent(parent, a)
    b_1 = find_parent(parent, b)
    if a_1 < b_1:
        parent[b] = a_1
    else:
        parent[a] = b_1


graph = []
ans = []
N, M = map(int, input().split())
parent = [0] * (N+1)
for i in range(N):
    parent[i] = i

for i in range(M):
    a, b, c = map(int, input().split())
    union(parent, a,b)
    graph.append((c, a, b))

graph.sort()
for c,a,b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        ans.append(c)

max = max(ans)
print(max)
print(ans)
print(sum(ans)-max)