"""
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
"""
import random

# 1 вариант
#
# list_1 = [random.randint(1, 100) for i in range(10)]
# k = 0
# print(list_1)
# # k = [i for i in range(0, 9) if (i - 1 < i > i): k += 1]
# for i in range(0, len(list_1) - 1):
#     if list_1[i - 1] < list_1[i] > list_1[i + 1]:
#         k += 1
# print(k)

# 2 вариант

my_list = [random.randint(1, 100) for i in range(5)]
size = len(my_list)
print(my_list)
count = 0
for i in range(size):
    if my_list[(i - 1) % size] < my_list[i % size] > my_list[(i + 1) % size]:
        count += 1
        print(my_list[i % size])
print(count)
