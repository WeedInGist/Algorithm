def turn(key):
    temp = []
    temp.append([-1,-1,-1])
    temp.append([-1,-1,-1])
    temp.append([-1,-1,-1])
    temp[0][0] = key[2][0]
    temp[0][1] = key[1][0]
    temp[0][2] = key[0][0]
    temp[1][0] = key[2][1]
    temp[1][2] = key[0][1]
    temp[2][0] = key[2][2]
    temp[2][1] = key[1][2]
    temp[2][2] = key[0][2]
    temp[1][1] = key[1][1]
    return temp
def move(key, x,y):
    temp = [[0,0,0,0,0,0,0,0,0] for _ in range(9)]
    for i in range(3,6):
        for j in range(3,6):
            temp[i][j] = key[i-3][j-3]
    ans = [[0,0,0,0,0,0,0,0,0] for _ in range(9)]
    for i in range(3,6):
        for j in range(3,6):
            ans[i+x][j+y]=temp[i][j]
    real = []
    real.append(ans[3][3:6])
    real.append(ans[4][3:6])
    real.append(ans[5][3:6])
    return real
def solution(key, lock):
    temp = key
    for i in range(4):
        temp = turn(temp)
        for x in range(-3,4):
            for y in range(-3,4):
                cand = move(temp,x,y)
                for a in range(3):
                    for b in range(3):
                        if cand == lock:
                            print("true")
                            return
    print("false")

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# solution(key,lock)
print(key)
print(move(key,3,3))
print(key)