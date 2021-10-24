n = int(input())

count = 0
once = True
for i in range(n+1):
    for k in range(60):
        for j in range(60):
            time = str(i)+str(k)+str(j)
            for z in time:
                if z == '3':
                    count += 1
                    break
print(count)