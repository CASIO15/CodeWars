import re                                                                        
                                                                                 
def decipher_this(string):                                                       
                                                                                 
    new_lst = []                                                                 
    final_lst = []                                                               
    result = []                                                                  
                                                                                 
    for i in re.findall(r'[0-9]+', string):                                      
        if i in string:                                                          
            new_lst.append(string.replace(i, chr(int(i))).split())               
                                                                                 
    for i in range(len(new_lst)):                                                
        final_lst.append(new_lst[i][i])                                          
                                                                                 
    for i in final_lst:                                                          
        try:                                                                     
            if len(i) > 2:                                                       
                result.append(i[0] + i[-1] + i[2:-1] + i[1])                     
            else:                                                                
                result.append(i)                                                 
        except:                                                                  
            result.append(i)                                                     
                                                                                 
    return ' '.join(result)                                                      
                                                                                 
print(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"))         
# result = The more he saw the less he spoke                                     
                                                                                 
