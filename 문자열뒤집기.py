s = input()
count = 0
current = s[0]
for i in s:
    if current != i:
        count += 1
        current = i

print(count//2)