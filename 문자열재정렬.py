S = input()
string = []
sum = 0
for i in S:
    if ord(i) > ord('9'):
        string.append(i)
    else:
        sum += int(i)
string.append(str(sum))
print(''.join(string))