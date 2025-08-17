'''
There are four types of number system:-
binary(0,1)
octal(0,1,2,3,4,5,6,7)
decimal(0,1,2,3,4,5,6,7,8,9)
Hexadecimal(0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F)

There are only two methods of conversion:-
1. Any to Decimal
2. Decimal to Any

In order to convert any number system to any other than decimal
Any --> Decimal --> Any

First we have to create two methods that convert any decimal number to decimal
To convert any number system to decimal
we follow the following steps:-

101101010
initial number system =  2
Starting from the Right most term, multiplying each term with 2^n 
    and n increases by 1 for each iterations we move towards left.
example:-
10110 to decimal => 1*2^4 + 0*2^3 + 1*2^2 + 1*2^1 + 0*2^0
for octal change 2 with 8
for hexa change 2 with 16 

In order to convert decimal number into any number system
Decimal --> Any

'''

def getDict():
    #this function creates returns the dictionary which contains keys from 0 to 15 and values from 0 to 9 & A to F as str
    import string

    #creating key values
    key_list = []
    for i in range(16):
        key_list.append(i)

    #creating column values
    value_list = []
    for i in range(10):
        value_list.append(str(i))
    first_six_alpha = list(string.ascii_uppercase[0:6])
    value_list=value_list+first_six_alpha

    #creating dictionary
    element_value_dictionary = {}
    for i in range(16):
        element_value_dictionary[value_list[i]] = key_list[i]

    return element_value_dictionary

def any_to_decimal(number,base):
    current_dict = getDict()

    #size of number:-
    size = len(str(number))
    number_str = str(number)
    sum=0
    for i in range(1,size+1):
        current_number = number_str[-i]
        if current_number.isdigit==False:
            current_number=current_number.upper()
        current_iteration = current_dict[str(current_number)]
        # print(f"{current_iteration} ,  type = {type(current_iteration)}")

        to_add = current_iteration * base ** (i-1)
        sum=sum+to_add

    return sum
def decimal_to_any(number, base):
    current_dict = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    remainder_list = []
    to_divide = number

    while to_divide >= base:
        remainder = to_divide % base
        if remainder < 10:
            remainder_list.append(str(remainder))
        else:
            remainder_list.append(current_dict[remainder])
        to_divide //= base

    # handle last digit
    if to_divide < 10:
        remainder_list.append(str(to_divide))
    else:
        remainder_list.append(current_dict[to_divide])

    # reverse to get the correct order
    remainder_list = remainder_list[::-1]

    return "".join(remainder_list)

    
def any_to_any(number,initial_base,final_base):
    first_step = any_to_decimal(number,initial_base)
    second_step = decimal_to_any(first_step,final_base)
    #print(f"Answer : {second_step}")
    return second_step




