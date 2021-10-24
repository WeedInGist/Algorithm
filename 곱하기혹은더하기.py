s = input()
li = []
for i in s:
    li.append(int(i))
ans = 1
if li[0] == 0:
    for i in range(1, len(li)):
        ans *= li[i]
else:
    for i in range(0, len(li)):
        ans *= li[i]
print(ans)