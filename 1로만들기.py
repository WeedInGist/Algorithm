def maker(x, dp):
    if x == 1:
        return 0
    if dp[x]nsdp == 0:
        if x % 5 == 0:
            min_1 = maker(x//5, dp)
        else:
            min_1 = 999999
        if x % 3 == 0:
            min_2 = maker(x//3, dp)
        else:
            min_2 = 999999
        if x % 2 == 0:
            min_3 = maker(x//2, dp)
        else:
            min_3 = 999999
        if x > 1:
            min_4 = maker(x-1, dp)
        else:
            min_4 = 999999
        min_ = min(min_1, min_2, min_3, min_4)
        dp[x] = 1 + min_
        return dp[x]
    return dp[x]
X = int(input())
dp = []
for i in range(X+1):
    dp.append(0)
result = maker(X, dp)
print(result)