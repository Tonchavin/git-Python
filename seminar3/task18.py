"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random

number = int(input('Введите размер списка: '))
find_number = int(input("Введите искомое число:"))

number_list = [random.randint(1, 10) for i in range(number)]
print(number_list)
count = 1
number_min = 0

if find_number > number or find_number == number:
    for j in range(1, len(number_list)):
        number_list[j - 1] <= number_list[j]
        if number_min <= number_list[j]:
            number_min = number_list[j]
else:
    for i in range(len(number_list)):
        if find_number != number_list[i]:
            if find_number + count == number_list[i]:
                number_min = number_list[i]
                break
            else:
                count -= 1
            if find_number - count == number_list[i]:
                number_min = number_list[i]
                break
            else:
                count += 1
print(number_min)

# 2 вариант
# my_list = [random.randint(0, 100) for i in range(20)]
# print(my_list)
#
# number = int(input('Введите число: '))
#
# near_number = my_list[0]
# range_number = abs(number - near_number)
#
# for num in my_list:
#     if abs(num - number) < range_number:
#         range_number = abs(num - number)
#         near_number = num
# print(f'Ближайшее число к {number} является {near_number}')