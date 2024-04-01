def combinations_b(arr, sides):
    result = []
    n = len(arr)
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if (i & (1 << j)) != 0:
                temp.append(arr[j])
        if len(temp) == sides:
            result.append(temp)
    return result

def combinations_a(arr, sides):
    result = []
    n = len(arr)
    for i in range(int(n ** sides)):
        temp = []
        t = i
        for j in range(sides):
            index = t % n
            temp.append(arr[index])
            t //= n
        result.append(temp)
    return result

def check_maps(possibles_a, possibles_b, map_probabilities):
    generated_probability = find_probabilities(possibles_a, possibles_b)
    return map_probabilities == generated_probability

def find_probabilities(dice_a, dice_b):
    result = {}
    for num1 in dice_a:
        for num2 in dice_b:
            sum_ = num1 + num2
            result[sum_] = result.get(sum_, 0) + 1
    return result

num1 = [1, 2, 3, 4]
num2 = [1, 2, 3, 4, 5, 6, 7, 8]
sides = 6
dice_a = [1, 2, 3, 4, 5, 6]
dice_b = [1, 2, 3, 4, 5, 6]
possibles_a = combinations_a(num1, sides)
possibles_b = combinations_b(num2, sides)

map_probabilities = find_probabilities(dice_a, dice_b)

flag = 0
for p1 in possibles_a:
    for p2 in possibles_b:
        if check_maps(p1, p2, map_probabilities):
            print("New Die A:", p1)
            print("New Die B:", p2)
            flag = 1
            break
    if flag == 1:
        break