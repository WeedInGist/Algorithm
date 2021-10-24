n = int(input())
num_list = list(map(int, input().split()))
d = []
for i in range(n):
    d.append(0)
def make(n):
    if n < 0:
        return 0
    if n == 0:
        return num_list[0]
    if n == 1:
        return num_list[1]
    if d[n] == 0:
        d[n] = num_list[n] + max(make(n-2), make(n-3))
        return d[n]
    else:
        return d[n]
print(max(make(n-1), make(n-2)))