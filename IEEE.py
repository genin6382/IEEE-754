import math
def convertToIEEE(num,precision_type):   
    if (float(num) == 0):
        handlingzero(num, precision_type)
        return ""
    #assigning the sign bit
    sign_bit = '0' if float(num) > 0 else '1'
    if (sign_bit == '1'):
        #removing the negative sign
        num=num[1:]
    #checking if the number is a float
    if '.' in num:
        result= binary(num)
        dot_index = result.index(".")
        one_index = result.index("1")
        if dot_index > one_index:
            exp = (dot_index-one_index)-1
        else:
            exp = dot_index - one_index
        mantissa = (result[one_index+1:]).replace(".","")
    #When the number is an integer
    elif(type(num) == int):
       result= intTobin(num)
       exp = len(result) - 1
       mantissa = result[1:]
       mantissa = mantissa.replace(".","")
    #To handle invalid inputs
    else:
        print("Not a valid number")
    if (precision_type == 1):
        singleprecision(exp,mantissa,sign_bit)
    elif (precision_type == 2):
        doubleprecision(exp,mantissa,sign_bit)

def handlingzero(num, precision_type):
    if num.startswith('-'):
        sign = '1'
    else:
        sign = '0'
    if precision_type==1:
        print(sign+"| 00000000|00000000000000000000000")
    elif precision_type==2:
        print(sign+ "|00000000000|0000000000000000000000000000000000000000000000000000")
#converting integer to binary
def intTobin(number):
    bin_int = 0
    i = 0
    number = int(number)
    while (number != 0):
        rem = number % 2
        number //= 2
        bin_int += (rem * 10**i)
        i += 1
    return str(bin_int)
#adds the binary part of integer and float together
def binary(num):
    num_float = float(num) 
    int_part = math.floor(num_float)
    bin_result = intTobin(int_part)
    float_part = num_float - int_part
    fin ='.'
    while (float_part!= 0):
            float_part *= 2
            fin += str(abs((int(float_part))))
            float_part-= int(float_part)
    final = bin_result+fin
    return final

def singleprecision(exponent,mantissa,sign_bit):
    biased_exponent = exponent + 127  #biasing the exponent
    bin_biased_exponent = intTobin(biased_exponent)   #converting the biased exponent to binary
    zeroes_toadd = 8 - len(bin_biased_exponent) 
    bin_biased_exponent=("0"*zeroes_toadd)+(bin_biased_exponent)  #adding zeroes to the exponent to make it 8-bit
    zeroes_toadd2= 23 - len(mantissa) 
    biased_mantissa = mantissa + ("0"*zeroes_toadd2) #adding zeroes to the mantissa to make it 23-bit
    biased_mantissa = biased_mantissa[:23]
    print(sign_bit + "|" + bin_biased_exponent + "|" + biased_mantissa)

def doubleprecision(exponent,mantissa,sign_bit):
    biased_exponent = exponent + 1023 #biasing the exponent
    bin_biased_exponent = intTobin(biased_exponent)
    zeroes_toadd = 11 - len(bin_biased_exponent)
    bin_biased_exponent=("0"*zeroes_toadd)+(bin_biased_exponent) #adding zeroes to the exponent to make it 11-bit
    zeroes_toadd2= 52 - len(mantissa)
    biased_mantissa = mantissa + ("0"*zeroes_toadd2) #adding zeroes to the mantissa to make it 52-bit
    biased_mantissa = biased_mantissa[:52]
    print(sign_bit + "|" + bin_biased_exponent + "|" + biased_mantissa)
    
    
#_main_
ch="y"
while(ch=="y"):
    num = input("Enter a number: ")
    precision_type = int(input("Enter: \n1 for Single precision representation\n2 for Double precision representation\n")) 
    convertToIEEE(num,precision_type)
    ch=input("Do you want to continue? y/n: ")