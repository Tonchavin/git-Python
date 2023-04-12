phone_book = []
start_phone_book = []
PATH = 'F:\Less_CZN\git-Python\seminar9\phone_book.txt'


def get_pb():
    return phone_book


def load_file():
    global start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split('|')
        phone_book.append({'name': contact[0], 'family': contact[1], 'phone': contact[2], 'comment': contact[3]})
    start_phone_book = phone_book.copy()


def save_file():
    data = []
    for contact in phone_book:
        data.append('|'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    phone_book.append(contact)


def exit_pb() -> bool:
    global phone_book, start_phone_book
    if phone_book == start_phone_book:
        return False
    else:
        return True


def find_contact(contact: dict):