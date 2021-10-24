n = input()
length = len(n)
half = len(n)//2
sum_left = 0
sum_right = 0
for i in range(0,half):
    sum_left += int(n[i])
for i in range(half, length):
    sum_right += int(n[i])
if sum_right == sum_left:
    print("LUCKY")
else:
    print("READY")
