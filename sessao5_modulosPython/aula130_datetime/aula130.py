# https://docs.python.org/3.0/library/datetime.html


from datetime import datetime, timedelta
from locale import setlocale, LC_ALL
from calendar import mdays

# strptime(str,format)
# .strftime(format)
# timestamp
# .fromtimestamp()


# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

# data = datetime.strptime('20/04/2019', '%d/%m/%Y')
# 1555729200.0

# data = datetime.fromtimestamp(1555729200.0)

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
print(data)
data = data + timedelta(days=5, seconds=59 * 60)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print('#' * 30)

data1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = data2 - data1
print(dif)
print(data1.time())

print(data2 > data1)
print('#' * 60)

setlocale(LC_ALL, 'pt_BR.utf-8')
# Sexta, 13 de Junho de 2019
dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)
print(mes_atual)
print(mdays)
print(mdays[mes_atual])
