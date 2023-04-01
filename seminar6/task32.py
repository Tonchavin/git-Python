"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
import random

number_start = int(input('Введите начало диапазона: '))
number_stop = int(input('Введите конец диапазона:'))

my_list = [random.randint(1, 100) for i in range(10)]
my_list.sort()
print(my_list)
for i in range(len(my_list)):
    if number_start <= my_list[i] <= number_stop:
        print(my_list[i], end=' ')
