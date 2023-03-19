"""
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
больших предыдущего (элемента с предыдущим номером)
"""
import random

count = 0
number = int(input('Введите размер списка: '))
number_list = [random.randint(0, 10) for _ in range(number)]
new_number_list = [i for i in range(1, len(number_list)) if number_list[i - 1] < number_list[i]]
print(number_list)
print(len(new_number_list))

# 2 - вариант
# count = 0
# for i in range(1, len(number_list)):
#     if number_list[i - 1] < number_list[i]:
#         count += 1
# print(count)
