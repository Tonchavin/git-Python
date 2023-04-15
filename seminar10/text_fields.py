main_menu = '''Главное меню:
            1. Открыть файл
            2. Сохранить файл
            3. Показать все контакты
            4. Создать контакт
            5. Найти контакт
            6. Изменить контакт
            7. Удалить контакт
            8. Выход'''

choice_menu = '\nВыберите пункт меню: '

empty_list_or_not_open_file = 'Телефонная книга пуста или файл не открыт!'

successful_open = 'Файл открыт успешно'
successful_save = 'Файл сохранен успешно'


def successful_edited(name: str) -> str:
    return f'Контакт {name} успешно изменен!'


new_name = 'Введите имя контакта: '
new_phone = 'Введите телефон контакта: '
new_comment = 'Введите комментарий к контакту: '


def contact_saved(name: str) -> str:
    return f'Контакт {name} успешно сохранен!'


def not_found(word: str) -> str:
    return f'Контакт по поиску {word} не найден '


input_keyword = 'Введите данные для поиска: '

input_index = 'Введите номер изменяемого контакта: '

enter_or_empty = 'Введите новые значения или оставьте пустым для сохранения оригинального'

input_delete_index = 'Введите индекс контакта который хотите удалить: '


def delete_contact(name: str) -> str:
    return f'Контакт {name} успешно удален!'


def confirm_delete(name: str) -> str:
    return f'Вы точно хотите удалить контакт {name}?'


# is_changed = 'Были внесены изменения. Сохранить? '

goodbye = 'До свидания! Всего хорошего'

no_saved_book = 'В телефонной книге есть не сохраненные изменения! Сохранить?'
