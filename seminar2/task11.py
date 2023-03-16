"""
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
"""

numbers = int(input('Введите число: '))
count = 2
fibonachi = 0
fibonachiN_1 = 1
fibonachiN_2 = 1

while fibonachi < numbers + 1:
    fibonachi = fibonachiN_1 + fibonachiN_2
    fibonachiN_1 = fibonachiN_2
    fibonachiN_2 = fibonachi
    count += 1
    if fibonachi == numbers:
        print(f'число {numbers} является числом фибоначи с индексом {count}')
        break
else:
    print(f'Число {numbers} не является числом фибоначи')
