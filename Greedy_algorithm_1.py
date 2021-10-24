n = int(input("금액을 입력하세요. : "))
coin_types = [500,100,50,10]
coins = 0
for coin in coin_types:
    coins += n//coin
    n %=coin
print(coins)
