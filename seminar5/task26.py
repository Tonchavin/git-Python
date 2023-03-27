"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""
numbers = int(input("Введите число: "))
degree_number = int(input("Введите степень: "))


def degree(numbers, degree_number):
    if degree_number == 1:
        return numbers
    return numbers * degree(numbers, degree_number - 1)

print(degree(numbers, degree_number))
