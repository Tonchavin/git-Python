"""
Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
"""
from random import random

number_shift = int(input("Введите число: "))
numbers_list = [i for i in range(10)]  # i можно заменить на _ (_ - это нейминг неважных переменных)
print(numbers_list)
print()
print(numbers_list[-number_shift:] + numbers_list[:-number_shift]) # сдвиг вправо
print()
print(numbers_list[number_shift:] + numbers_list[:number_shift]) # сдвиг влево
# numbers_list = numbers_list[-number_shift:] + numbers_list[:-number_shift] # Изменение содержимого списка
# print(numbers_list)
# print()
# 2 - Вариант
# for i in range(number_shift):
#     numbers_list.insert(0, numbers_list.pop())
# print(numbers_list)
