"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
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
