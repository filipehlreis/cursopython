"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
#
# b = 0
#
# for a in range(9):
#     print(a, 10 - b)
#     b += 1
#
# a = 0
# b = 10
# print('\n\n')
# while a < 9 and b > 1:
#     print(a, b)
#     a, b = a + 1, b - 1

"""
Solucao
###############################
"""

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
