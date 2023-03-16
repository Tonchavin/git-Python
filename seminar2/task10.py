"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
"""
from random import randint

count_money = int(input("Введите количество монет: "))
temp = 0
temp_zero = 0
temp_one = 0

for i in range(count_money):
    temp = randint(0, 1)
    print(temp, end=" ")
    if temp == 0:
        temp_zero += 1
    else:
        temp_one += 1
if temp_zero > temp_one:
    print(f'\n{temp_one} монеток с гербом нужно перевернуть')
else:
    print(f'\n{temp_zero} монеток с решкой нужно перевернуть')

"""
Эталонное решение
"""
n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
if x == 0:
    count_zero += 1
else:
    count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)
