def check_empty_list(li):
    for i in range(len(li)):
        if li[i] != 0:
            return False
    return True


def solution(food_times, k):
    food = len(food_times)
    index = 0
    while k >= 0:
        if check_empty_list(food_times) is False:
            if food_times[index] > 0:
                food_times[index] -= 1
                index += 1
                if k == 0:
                    return index
                else:
                    k -= 1
                if index == food:
                    index = 0
            else:
                index += 1
                if index == food:
                    index = 0
        else:
            if k >= 0:
                return -1

food_times = [3,1,2]
k = 5
print(solution(food_times, k))