# variavel = 'valor'
#
# # print(variavel)
#
#
# def func():
#     print(variavel)
#
#
# def func2():
#     global variavel
#     variavel = 'outro valor'
#     print(variavel)
#
# def func3(arg=None):
#     arg = arg.replace('v','c')
#     return arg
#
# func()
# func2()
# outra_variavel = func3(arg=variavel)
# print(outra_variavel)
#
#


variavel = 'valor'


def func():
    outra_variavel = 'valor'
    return outra_variavel

def func2(var):
    print(var)


var = func()
func2(var)
