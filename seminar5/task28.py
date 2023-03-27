"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
    4
"""
numb_one = int(input("Введите первое число: "))
numb_two = int(input("Введите второе число: "))

def summa(numb_one, numb_two):
    if numb_one == 0:
        return numb_two
    return summa(numb_one - 1, numb_two + 1)


print(summa(numb_one, numb_two))
