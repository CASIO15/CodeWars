def decode(arg):

    nums = ''
    letters = ''
    res = ''

    flag = False
    index = 0
    index_2 = 0

    ascii_enumerate = {v: e for e, v in enumerate('abcdefghijklmnopqrstuvwxyz')}
    ascii_enumerate_2 = {e: v for e, v in enumerate('abcdefghijklmnopqrstuvwxyz')}

    for i in arg:
        if i.isnumeric():
            nums += i
        else:
            letters += i

    while index < len(letters):
        if index_2 * int(nums) % 26 == ascii_enumerate[letters[index]]:
                res += ascii_enumerate_2[index_2]

        if flag:
            index += 1
            index_2 = 0
            flag = False

        else:
            index_2 += 1
            if index_2 == 25:
                flag = True

    if len(res) != len(letters):
        return 'Impossible to decode'
    else:
        return res



print(decode('761328qockcouoqmoayqwmkkic')) # 'Impossible to decode'
print(decode("6015ekx")) # mer 
