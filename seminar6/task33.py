"""
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
"""
import random

# 1 вариант
# my_list = [random.randint(0, 10) for i in range(10)]
# print(my_list)
# dict = {}
# count = 0
# for i in my_list:
#     dict[i] = dict.get(i, 0) + 1
# for key, value in dict.items():
#     count += value // 2
# print(count)

# 2 вариант

my_list = [random.randint(0, 10) for i in range(10)]
print(my_list)

count = 0
for item in range(len(my_list)):
    if my_list.count(item):
        count += my_list.count(item) // 2
print(count)
