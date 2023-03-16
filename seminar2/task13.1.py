"""
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
"""
from random import randint

count_melon = int(input("Введите количество арбузов: "))
min_weight_melon = 2
max_weight_melon = 1

for i in range(count_melon):
    weight = randint(1, 30)
    print(weight, end=" ")
    if min_weight_melon >= weight:
        min_weight_melon = weight
    if max_weight_melon <= weight:
        max_weight_melon = weight
print()
print(min_weight_melon, max_weight_melon)
