def getCode(value):
    key_list= ['Binary','Octal','Decimal','Hexadecimal']
    column_list = [2,8,10,16]
    
    mixed_dict = {}

    for i in range(4):
        mixed_dict[key_list[i]]=column_list[i]


    return mixed_dict[value]

