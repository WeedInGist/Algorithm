def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a_1 = find_root(parent, a)
    b_1 = find_root(parent, b)
    if a_1 < b_1:
        parent[b] = a_1
    else:
        parent[a] = b_1


def check(parent, a, b):
    if find_root(parent, a) == find_root(parent, b):
        print("YES")
    else:
        print("NO")


N, M = map(int, input().split())


parent = [0] * (N+1)
for i in range(N+1):
    parent[i] = i

for i in range(M):
    func, a, b = map(int, input().split())
    if func == 0:
        union(parent, a, b)
    else:
        check(parent, a, b)
