"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

import random

number_one = int(input('Введите размер: '))
number_two = int(input('Введите размер: '))
one_list = [random.randint(1, 10) for i in range(number_one)]
two_list = [random.randint(1, 10) for i in range(number_two)]
print(one_list)
print(two_list)

result = list(set(one_list) & set(two_list))
print(sorted(result))
