def jumping_number(number):
    
    res = []
    num = str(number)
    for i in range(len(num)-1):
        if int(num[i]) + 1 == int(num[i+1]) or int(num[i]) - 1 == int(num[i+1]):
            res.append(True)
    
        else:
            res.append(False)
        
    if all(res):
        return 'Jumping!!'

    else:
        return 'Not!!'
