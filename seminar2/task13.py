"""
1. Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
Их интересует, сколько дней длилась самая длинная оттепель.
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
Напишите программу, помогающую синоптикам в работе.

Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.

Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
"""

from random import randint

count_days = int(input("Введите количество дней: "))
count = 0
days = randint(-3, 3)

count_warm_day = 0
warm_day = 0

while count < count_days:
    days += randint(-3, 3)
    count += 1
    print(days, end=" ")
    if days > 0:
        warm_day += 1
        count_warm_day = warm_day
        if count_warm_day <= warm_day:
            count_warm_day = warm_day
    else:
        warm_day = 0
print(f"количество теплых дней подряд: {count_warm_day}")
