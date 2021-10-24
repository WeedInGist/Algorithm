condition = list(map(int, input().split()))
a = []
result = []
for i in range(condition[0]):
    a.append(list(map(int,input().split())))
for i in range(condition[0]):
    a[i].sort()
    result.append(a[i][0])
print(result[-1])
