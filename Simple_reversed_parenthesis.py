def solve(string):

    res = []

    index = 0
    final = 0

    if len(string) % 2 != 0:
        return -1

    else:
        for i in range(len(string)):
            new_str = filter(lambda x: x != '()', string.split('()'))
            string = ''.join(new_str)

    for _ in range(len(string)):
        res.append(string[index:index+2])
        index += 2

    for i in res:
        if i != '':
            if i == ')(':
                final += 2

            elif i == '))' or i == '((':
                final += 1

    return final
    
print(solve("())()))))()()(")) # 4
print(solve('())(((')) # 3
print(solve(')()(')) # 2
print(solve('(((())))')) # 0
