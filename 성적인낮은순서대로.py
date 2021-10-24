def setting(li):
    return int(li[1])


n = int(input())
a = []
for i in range(n):
    a.append(input().split())
sorted(a, key=setting)

for i in range(n):
    print(a[i][0], end=" ")
