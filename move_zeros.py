def move_zeros(array):
    result = []
    zeros = []

    for i in range(len(array)):
        if array[i] != 0 or type(array[i]) is bool:
            result.append(array[i])

    for i in range(len(array)):
        if array[i] == 0 and type(array[i]) is not bool:
            zeros.append(array[i])

    return result + zeros

print(move_zeros([False,1,0,1,2,0,1,3,'a']))
# Result = [False, 1, 1, 2, 1, 3, 'a', 0, 0]
