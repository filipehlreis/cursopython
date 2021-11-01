# t1 = (1, 2, 3, 'a', 'Filipe Henrique')
#
# print(t1[4])
# print(type(t1))
#
# for v in t1:
#     print(v)
#
#
#
# print(t1[2:])
# print(t1[1:2])
# print(t1[:2])
#
# t2 = 1,
# print(t2, type(t2))

#
# t1 = (1, 2, 'luiz', 4, 5) * 20
# # t2 = 6, 7, 8, 9, 10
# # t3 = t1 + t2
# #
# # n1, n2, n3, *_, nN = t3
# # print(nN)
#
# print(t1)


t1 = (1, 2, 3, 4, 5)

t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)
print(t1)
