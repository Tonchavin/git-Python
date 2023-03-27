"""
Последовательностью Фибоначчи, называется последовательность чисел a0, a1, ..., an, ..., где.Сделать рекурсией.
"""

# def fib(numbers):
#     if numbers == 1 or numbers == 0:
#         return 1
#     return fib(numbers - 1) + fib(numbers - 2)
# print(fib(7))

"""
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
"""

import math


def simple(num: int) -> bool:
    if num in [1, 2, 3]:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
        return True


print(simple(53))
