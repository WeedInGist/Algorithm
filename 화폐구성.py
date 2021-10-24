n,m = map(int,input().split())
price = []
for i in range(n):
    price.append(int(input()))
sorted(price)
d = [float("inf")] * (m+1)
d[0] = 0
sorted(d)
for i in range(n):
    for j in range(price[i],m+1):
        if d[j - price[i]] != float("inf"):
            d[j] = min(d[j], 1 + d[j-price[i]])
if d[m] == float("inf"):
    print("-1")
else:
    print(d[m])
