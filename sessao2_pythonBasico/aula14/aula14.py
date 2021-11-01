# import re
#
#
# def is_float(val):
#     if isinstance(val, float): return True
#     if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_int(val):
#     if isinstance(val, int): return True
#     if re.search(r'^\-{,1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_number(val):
#     return is_int(val) or is_float(val)
#




num1= input('digite um numero: ')
num2= input('digite um numero: ')

# isnumeric isdigit isdecimal
print(num1.isnumeric())
print(num1.isdecimal())
print(num1.isdigit())

# if is_number(num1) and is_number(num2):
try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

# else:
except:
    print('nao consegui realizar as contas')










