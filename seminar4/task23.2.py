import random

# my_list = [random.randint(0, 5) for i in range(20)]
# print(my_list)
# number = int(input('Введите число: '))
# print(f'Число {number} встречается в списке {my_list.count(number)} раз')

my_list = [random.randint(0, 100) for i in range(20)]
print(my_list)

number = int(input('Введите число: '))

near_number = my_list[0]
range_number = abs(number - near_number)

for num in my_list:
    if abs(num - number) < range_number:
        range_number = abs(num - number)
        near_number = num
print(f'Ближайшее число к {number} является {near_number}')