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

# Эталон решения

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
# if min_number <= list_1[i] <= max_number:
# print(i)