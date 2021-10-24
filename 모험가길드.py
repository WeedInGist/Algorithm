n = int(input())
fear = list(map(int, input().split()))
fear.sort()
group_num = 0
group = []
for i in range(fear[0], fear[-1]+1):
    count_num = 0
    for j in fear:
        if j == i:
            count_num += 1
    group.append((i, count_num))

left = 0
index = 0
for i in group:
    next_index = index + 1
    if index == len(group) -1:
        break
    group_num += i[1]//i[0]
    left = i[1]%i[0]
    group[next_index]=(group[next_index][0], group[next_index][1]+left)
    index += 1

print(group_num)