s = input()
coor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = 0
y = int(s[1])
for i in range(8):
    if s[0] == coor[i]:
        x = i+1
        break
count = 0
for j in range(8):
    for k in range(8):
        if ((j+1)-x)**2 + ((k+1)-y)**2 == 5:
            count+=1
print(count)
