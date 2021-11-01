"""
# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estao nos dois sets, mas nao em ambos)
"""

s2 = {1, 2, 3, 4, 5}
#
# print(s1)
#
# for v in s1:
#     print(v)

##############################################################################
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add((1, 2, 3, 'Luiz'))
#
# print(s1)
# s1.discard(2)
# print(s1)
##############################################################################
#
# s1 = set()
# s1.update('Python')
# print(s1)
# print()
#
# l1 = [1, 2, 11, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 'Luiz', 'Luiz']
# print(l1)
# l1 = set(l1)
# print(l1)
# l1 = list(l1)
# print(l1[-1])
##############################################################################


s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1|s2

print(s3)
print()

s3 = s1&s2

print(s3)
print()


s3 = s1-s2

print(s3)
print()


s3 = s1^s2

print(s3)
print()


##############################################################################
#
# l1 = ['Luiz', 'Joao', 'Maria']
# l2 = ['Luiz', 'Joao', 'Jorge', 'Maria', 'Maria', 'Maria', 'Joao', 'Maria', 'Joao', 'Maria']
#
# if set(l1) == set(l2):
#     print('L1 é igual de L2')
# else:
#     print('L1 é diferente de L2')
#
# print(l1 != l2)
#
# l1 = list(set(l1))
# l2 = list(set(l2))
# print(l1 != l2)
