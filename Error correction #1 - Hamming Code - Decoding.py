
def decoding_(string):
    
    index = 0
    new_lst = []
    corrected_bits = []

    for _ in string:
        if len(string[index:index+3]) == 3:
            new_lst.append(string[index:index+3])

        index += 3

    for i in new_lst:
        if i.count('1') > i.count('0'):
            corrected_bits.append('1')
        else:
            corrected_bits.append('0')


    joined_bits = ''.join(corrected_bits)
    joined_bits_lst = []
    new_index = 0
    result_str = ''

    for _ in joined_bits:
        if len(joined_bits[new_index:new_index+8]) == 8:
            joined_bits_lst.append(joined_bits[new_index:new_index+8])

        new_index += 8

    for i in joined_bits_lst:
        # int takes second arg, base
        result_str += chr(int(i, 2))

    return result_str
decoding('000111000111000111000000000000111111111111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111')
    # result = T?st!%
