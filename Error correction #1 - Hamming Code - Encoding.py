from string import punctuation

def encoding_(sting):
    
    str_lst = []
    changed_special = []
    final_result = []

    for i in string:

        if i in list(punctuation) or i.isdigit() or i == ' ':
            raw_bin = bin(ord(i)).replace('b', '')
            final_bin = raw_bin.zfill(len(raw_bin) + 3)
            final_result.append(final_bin[:3])

            for i in final_bin[3:]:
                for x in i:
                    final_result.append(x*3)
        else:
            raw_str = bin(ord(i)).replace('b', '')
            for i in raw_str:
                final_result.append(i*3)

    return ''.join(final_result)

encoding_('T?st!%')
# Result = 000111000111000111000000000000111111111111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111
