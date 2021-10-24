possible = True
N = int(input())
list_1 = list(map(int,input().split()))
M = int(input())
list_2 = list(map(int,input().split()))
sorted(list_1)
for i in range(M):
    if possible is False:
        break
    target = list_2[i]
    first = 0
    end = N-1
    while True:
        if first > end:
            possible = False
            break
        mid = (first + end) // 2
        if mid == target:
            break
        if list_1[mid] > target:
            end = mid - 1
        else:
            first = mid + 1
if possible:
    print("Yes")
else:
    print("No")