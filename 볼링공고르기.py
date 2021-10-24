n, m = map(int, input().split())

li = list(map(int,input().split()))
li.sort()
li.append(0)
count_group = 1
num = 0
tup = []
current = li[0]
for i in li:
    if i == current:
        num += 1
    else:
        tup.append((current, num))
        current = i
        num = 1
results = 0
for i in range(len(tup)):
    sum = 0
    for j in range(len(tup)):
        if i != j:
            sum += tup[j][1]
    results += sum*tup[i][1]
print(results/2)
