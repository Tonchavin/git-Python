"""
Дана упорядоченная последовательность an чисел от 1 до N.
Из копии данной последовательности bn удалили одно число, а оставшиеся перемешали. Найти удаленное число.
"""
import random

size_list = int(input("Введите размер: "))
number = int(input("Введите цифру которую удаляем: "))
number_list = [i for i in range(size_list)]
set_list = set(number_list)
print(number_list)
copy_number_list = number_list
copy_number_list.remove(number)
print(copy_number_list)
random.shuffle(copy_number_list)
print(copy_number_list)
print(set_list.difference(copy_number_list))
