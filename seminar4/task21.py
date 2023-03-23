"""
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
"""
import random
import string

# 1 Вариант

my_string = ''.join([random.choice(string.ascii_letters) for i in range(30)])
print(my_string)

count_dict = {}
for char in my_string:
    count_dict[char] = count_dict.get(char, 0) + 1
    if count_dict.get(char) > 1:
        print(f'{char}_{count_dict.get(char)} ', end=" ")
    else:
        print(char + ' ', end=" ")

# 2 Вариант
# number_list = list(input("Введите число: "))
# print(number_list)
#
# number_dict = dict()
# for item in set(number_list):
#     number_dict.setdefault(item, 1)
#
# for key, value in number_dict.items():
#     for i in range(len(number_list)):
#         if number_list[i] == key:
#             if value > 1:
#                 number_list[i] = f'{key}_{value}'
#             value += 1
# result = ''
#
# for i in number_list:
#     result += f'{i} '
#
# print(result)

# 3 Вариант

# in_str = input("Введите строку: ")
#
# dict_str = {"v": "3"}
#
# for i in in_str:
#     if i in dict_str:
#         print(f"{i}_{dict_str[i]}", end=" ")
#         dict_str[i] += 1
#     else:
#         dict_str[i] = 1
#         print(i, end=" ")
