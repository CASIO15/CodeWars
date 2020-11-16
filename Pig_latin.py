def pig_it(st):
    
    res = []

    for i in st.split(' '):
        if i.isalpha():
            new = i[0] + 'ay'
            st = i[1:] + new
            res.append(st)
        else:
            res.append(i)
    
    return ' '.join(res)
