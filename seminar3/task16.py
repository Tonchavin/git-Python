"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
"""
import random

number = int(input('Введите размер списка: '))
find_number = int(input("Введите искомое число:"))
number_list = [random.randint(1, 10) for i in range(number)]
print(number_list)

count = 0
for i in range(len(number_list)):
    if find_number == number_list[i]:
        count += 1
print(f"Число {find_number} встречается {count} раз")
