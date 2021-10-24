
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
x, y, di = map(int,input().split())
mapping = []
turn = 0
temp_x, temp_y = 0, 0
for i in range(N):
    mapping.append(list(map(int, input().split())))
visited = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(False)
    visited.append(temp)

visited[y][x] = True
count = 1
while True:
    di = (di + 3) % 4
    temp_y = y + directions[di][0]
    temp_x = x + directions[di][1]
    if turn == 4:
        if mapping[y - directions[di][0]][x - directions[di][1]] == 1:
            print(count)
            break
        else:
            y = y-directions[di][0]
            x = x-directions[di][1]
            turn = 0
            continue
    if (0 <= temp_x < M and 0 <= temp_y < N) is True:
        if mapping[temp_y][temp_x] == 0 and visited[temp_y][temp_x] == False:
            y = temp_y
            x = temp_x
            count += 1
            visited[y][x] = True
            turn = 0
        else:
            turn += 1
    else:

        turn += 1