"""
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""
import string

my_string = 'Пользователь вводит текст(строка).Текст. Словом считается последовательность непробельных символов идущих подряд.'
print(string.punctuation)

for char in string.punctuation:
    my_string = my_string.replace(char, ' ')
my_string = my_string.lower().split()
print(len(set(my_string)))

# 2 Вариант
# words = input("Введите строку: ").lower()
# string_words = words.split()
# count = 1
#
# for i in range(1, len(string_words)):
#     if string_words[i - 1] != string_words[i]:
#         count += 1
# print(count)
