"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
import random

number_start = int(input('Введите первое число: '))
number_step = int(input('Введите второе число:'))
number_count = int(input('Введите третье число:'))

my_list = []
for i in range(number_count):
    my_list.append(number_start)
    number_start += number_step
print(my_list)

# Эталон решения
#
# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
# print(a1 + i * d)