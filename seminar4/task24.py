"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
"""

import random

number_one = int(input('Введите размер: '))
one_list = [random.randint(1, 10) for i in range(number_one)]
temp = 0
result = 0
print(one_list)

for i in range(1, len(one_list) - 1):
    temp = one_list[i - 1] + one_list[i] + one_list[i + 1]
    print(one_list[i - 1], [i - 1], '+', one_list[i], [i], '+', one_list[i + 1], [i + 1], '=', temp)
    if temp > result:
        result = temp
else:
    print(one_list[number_one - 1], [number_one - 1], '+', one_list[0], [0], '+', one_list[1], [1], '=', temp)
    print(one_list[number_one - 2], [number_one - 2], '+', one_list[number_one - 1], [number_one - 1], '+', one_list[0],
          [0], '=', temp)
    if result < (one_list[number_one - 1] + one_list[0] + one_list[1]):
        result = one_list[number_one - 1] + one_list[0] + one_list[1]
        if result < (one_list[number_one - 2] + one_list[number_one - 1] + one_list[0]):
            result = one_list[number_one - 2] + one_list[number_one - 1] + one_list[0]
    print(result)

# Эталон решения
# n = int(input())
# arr = list()
# for i in range(n):
#     x = int(input())
#     arr.append(x)
#
# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[- 1] + arr[0])
# print(max(arr_count))
