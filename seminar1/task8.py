"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
print('Введите размеры шоколадной плитки: ')
rows = int(input())
columns = int(input())
cut_count = int(input('Введите сколько хотите отломить плиток шоколада: '))

if (rows == 1 or columns == 1) and (cut_count < rows or cut_count < columns) and (rows != columns):
    print(f'Вы можете {cut_count} отломить')
if cut_count > 1 and cut_count % 2 == 0:
    print(f'Вы можете {cut_count} отломить')
else:
    print(f'Вы не можете {cut_count} отломить')
