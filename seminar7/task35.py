import random

# numbers = '123456789'
# numbers = list(numbers)
# print(numbers)
# numbers = list(map(int, numbers))
# numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(numbers)

# numbers = [random.randint(0, 100) for i in range(10)]
# print(numbers)
#
# for i, item in enumerate(numbers, 10): # 10 - начала нумерации(с какого числа начинается), если убрать то с 0
#     if item > 50:
#         print(i, end=' ')

# numbers = [random.randint(0, 100) for i in range(10)]
# letters = list('fghrytdkhi')
# print(numbers)
# print(letters)
# final = list(zip(numbers, letters))
# print(final)


print((lambda x, y, z: x + y + z)(1, 2, 3))

# Пример поиска
# text = 'аываыдвжыоджпжып'
# list_tup = 'ывыап'
# for char in text:
#     if char in list_tup:
#         print(char, end=' ')