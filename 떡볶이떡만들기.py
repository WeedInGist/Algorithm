N, M = map(int, input().split())
rice_list = list(map(int, input().split()))

start = 0
end = max(rice_list)

result = 0
total = 0
while True:
    mid = (start+end)//2
    for i in rice_list:
        total += i-mid
    if total > M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
