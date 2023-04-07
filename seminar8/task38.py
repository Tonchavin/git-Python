"""
Написать программу для работы с телефонным словарем, предварительно его создав.
"""
import shutil

print('Меню тел.справочника: \n1 - Показать тел.справочник \n2 - Добавить новую запись в тел.справочник '
      '\n3 - Редактировать тел.справочник \n4 - Поиск в тел.справочнике \n5 - Удалить запись из тел.справочника')


# src = 'F:\Less_CZN\git-Python\seminar8\phone.txt'
# dest = 'F:\Less_CZN\git-Python\seminar8\phone_copy.txt'
# shutil.copy2(src, dest)

# shutil.copy2(src, dest)
def in_print_phone():
    file_phone = open('F:\Less_CZN\git-Python\seminar8\phone.txt', 'r', encoding='UTF-8')
    phone = file_phone.read()
    print('Phone|            FIO         |Address|House|Corps|Room|')
    print('________________________________________________________')
    print(phone)
    file_phone.close()


def in_add_new_line_phone():
    file_phone = open('phone.txt', 'a', encoding='UTF-8')  # открытие в режиме записи
    new_line = input('Введите новую запись через пробел(Phone FIO Address House Corps Room): ').split()
    temp_line_start = "|".join(new_line[:1]) + str('|')
    temp_line_medium = " ".join(new_line[1:4]) + str('|')
    temp_line_end = "|".join(new_line[4:]) + str('|')
    temp_line = temp_line_start + temp_line_medium + temp_line_end
    file_phone.write(f'\n{temp_line}')  # запись в файл с новой строки
    file_phone.close()  # закрытие файла


def in_fix_line_phone():
    file_phone = open('F:\Less_CZN\git-Python\seminar8\phone.txt', 'r+', encoding='UTF-8')
    phone = file_phone.readlines()
    file_phone.close()
    # print(*[item + '\n' for item in phone])
    find_word = input('Введите поисковые данные через пробел: ')
    in_index_line = []
    for in_find_word in phone:
        if find_word in in_find_word:
            print('          Phone|          FIO           |Address|House|Corps|Room|')
            print('          ________________________________________________________')
            print(f'Найдено: ', in_find_word)
            print('Номер строки', phone.index(in_find_word))
            in_index_line.append(phone.index(in_find_word))
    index_line = int(input('Введите номер строки которую хотите изменить: '))
    print(phone[index_line])
    new_line = input('Введите новую запись через пробел(Phone FIO Address House Corps Room): ').split()
    temp_line_start = "|".join(new_line[:1]) + str('|')
    temp_line_medium = " ".join(new_line[1:4]) + str('|')
    temp_line_end = "|".join(new_line[4:]) + str('|')
    temp_line = temp_line_start + temp_line_medium + temp_line_end
    phone.remove(phone[index_line])
    phone.insert(index_line, temp_line + '\n')
    file_phone = open('F:\Less_CZN\git-Python\seminar8\phone.txt', 'w', encoding='UTF-8')
    file_phone.write(''.join(map(str, phone)))  # запись в файл с новой строки
    file_phone.close()


def in_find_phone():
    file_phone = open('F:\Less_CZN\git-Python\seminar8\phone.txt', 'r', encoding='UTF-8')
    find_word = input('Введите поисковые данные: ')
    phone = file_phone.readlines()
    for in_find_word in phone:
        if find_word in in_find_word:
            print('          Phone|          FIO           |Address|House|Corps|Room|')
            print('          ________________________________________________________')
            print(f'Найдено: ', in_find_word)
    file_phone.close()


def in_del_line_phone():
    file_phone = open('F:\Less_CZN\git-Python\seminar8\phone.txt', 'r+', encoding='UTF-8')
    phone = file_phone.readlines()
    file_phone.close()
    find_word = input('Введите поисковые данные через пробел: ')
    in_index_line = []
    for in_find_word in phone:
        if find_word in in_find_word:
            print('          Phone|          FIO           |Address|House|Corps|Room|')
            print('          ________________________________________________________')
            print(f'Найдено: ', in_find_word)
            print('Номер строки', phone.index(in_find_word))
            in_index_line.append(phone.index(in_find_word))
    index_line = int(input('Введите номер строки которую хотите удалить: '))
    print(phone[index_line])
    phone.remove(phone[index_line])
    file_phone = open('F:\Less_CZN\git-Python\seminar8\phone.txt', 'w', encoding='UTF-8')
    file_phone.write(''.join(map(str, phone)))  # запись в файл с новой строки
    file_phone.close()


number_main_phone = int(input('Введите нужную цифру: '))
if number_main_phone == 1:
    in_print_phone()
if number_main_phone == 2:
    in_add_new_line_phone()
if number_main_phone == 3:
    in_fix_line_phone()
if number_main_phone == 4:
    in_find_phone()
if number_main_phone == 5:
    in_del_line_phone()
