"""
Написать программу для работы с телефонным словарем, предварительно его создав.
"""

print('Меню тел.справочника: \n1 - Показать тел.справочник \n2 - Добавить новую запись в тел.справочник '
      '\n3 - Редактировать тел.справочник \n4 - Поиск в тел.справочнике \n5 - Удалить запись из тел.справочника')


def in_print_phone():
    file_phone = open('phone.txt', 'r', encoding='UTF-8')
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


def in_find_phone():


def in_del_line_phone():


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
