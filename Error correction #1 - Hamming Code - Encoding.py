from string import punctuation

string = 'T?st!%'


str_lst = []
changed_special = []
final_special = []


for i in string:

    if i in list(punctuation) or i.isdigit() or i == ' ':
        raw_bin = bin(ord(i)).replace('b', '')
        final_bin = raw_bin.zfill(len(raw_bin) + 3)
        final_special.append(final_bin[:3])

        for i in final_bin[3:]:
            for x in i:
                final_special.append(x*3)
    else:
        raw_str = bin(ord(i)).replace('b', '')
        for i in raw_str:
            final_special.append(i*3)

print(''.join(final_special))


# Result = 000111000111000111000000000000111111111111111111000111111111000000111111000111111111000111000000000000111000000000000111000000111000000111000111
