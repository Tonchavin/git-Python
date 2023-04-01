"""
Даны два массива чисел.
Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""

import random
# 1 Вариант
# number_one = int(input('Введите размер: '))
# number_two = int(input('Введите размер: '))
# list_one = [random.randint(1, 100) for i in range(number_one)]
# list_two = [random.randint(1, 100) for i in range(number_two)]
# print(list_one)
# print(list_two)
# list_three = [item for item in list_one if item not in list_two]
# print(list_three)

# for item in list_one:
#     if item not in list_two:
#         print(item, end=" ")

# 2 Вариант
print('Необходимо ввести -> 1: Длинна списка 1 2: Длинна списка 2 3: Число мин 4: Число мах')
my_vars = tuple(map(int, input('Введите числа через пробел: ').split()))
my_list1 = [random.randint(my_vars[2], my_vars[3]) for i in range(my_vars[0])]
my_list2 = [random.randint(my_vars[2], my_vars[3]) for i in range(my_vars[0])]
my_list3 = [item for item in my_list1 if item not in my_list2]
print(my_list1)
print(my_list2)
print(my_list3)