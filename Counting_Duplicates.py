from numbers import Number

def duplicate_count(string):
    new_dict = {}
    new_lst = []

    for i in string.lower():
        if i.isalpha() or isinstance(int(i), Number):
            new_dict[i] = string.lower().count(i)

        else:
            pass
    for k, v in new_dict.items():
        if v > 1:
            new_lst.append(k)

    return len(new_lst)

print(duplicate_count('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZReturnsTwentySix'))
# Result = 26
