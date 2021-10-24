size_n = int(input())
plan = input().split()

cur_x, cur_y= 1,1
next_x, next_y = 0,0
for i in range(len(plan)):
    if plan[i] == 'D':
        next_x = cur_x + 1
        if 1 <= next_x <= size_n:
            cur_x= next_x
    if plan[i] == 'U':
        next_x = cur_x - 1
        if 1 <= next_x <= size_n:
            cur_x= next_x
    if plan[i] == 'L':
        next_y = cur_y - 1
        if 1 <= next_x <= size_n:
            cur_y= next_y
    if plan[i] == 'R':
        next_y = cur_y + 1
        if 1 <= next_y <= size_n:
            cur_y= next_y
print(cur_x,cur_y)