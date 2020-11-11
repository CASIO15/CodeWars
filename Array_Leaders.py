def array_leaders(numbers):

    res_arr = []

    for i in range(len(numbers)):
        if numbers[i] > sum(numbers[i+1:]):
            res_arr.append(numbers[i])

    return res_arr

print(array_leaders([1,2,3,4,0]))
print(array_leaders([16,17,4,3,5,2]))
print(array_leaders([-1,-29,-26,-2]))
print(array_leaders([-36,-12,-27]))

# Results :
[4]
[17, 5, 2]
[-1]
[-36, -12]
