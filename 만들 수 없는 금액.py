n = list(map(int,input().split()))
n.sort()
price = 1
while True:
    for x in n:
        if price < x:
            break
        price += x
print(price)