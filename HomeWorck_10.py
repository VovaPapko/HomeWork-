from collections import UserDict


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Try help'
        except ValueError:
            return 'Invalid value. Try again'
        except KeyError:
            return 'Contact not found. Try again'
    return inner


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self) -> str:
        return str(self)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phones = [phone] if phone else None

    def add_phone(self, phone):
        self.phones.append(phone)
        return f'Phone {phone} successfully added'

    def change_phone(self, index, phone):
        self.phones[index] = phone
        return f'Phone {phone} successfully changed'

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def __str__(self) -> str:
        return f'{str(self.name)} {", ".join([str(p) for p in self.phones])}'


class AddressBook(UserDict):

    def add_record(self, record):
        name = record.name.value
        self.data[name] = record

    def show_all(self):
        return '\n'.join([str(rec) for rec in self.data.values()])


contacts = AddressBook()


def help(*args):
    return '''
    "hello", "How can I help you?"

    "help" список команд

    "add ...". Додає ім'я та номер телефону, через пробіл.

    "change..." Змінює котактні дані через пробіл.

    "phone ...." Виводить у консоль контактні дані по номеру телефону

    "show all". Показує всі контакти.

    "good bye", "close", "exit"  "Good bye!".
    '''


def hello(*args):
    return '''How can I help you?'''


def exit(*args):
    return '''Good Bye'''


def no_command(*args):
    return '''Unknown command, try again'''


def show_all(*args):
    return contacts.show_all()


@input_error
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = contacts.get(str(name))
    if rec:
        return rec.add_phone(phone)
    record = Record(name, phone)
    contacts.add_record(record)
    return f"Added <{name.value}> with phone <{phone.value}>"


@input_error
def phone(*args):
    name = Name(args[0])
    rec = contacts.get(name.value)
    if rec:
        return rec.phones
    return f'There are no phones with name {name}'


def change(*args):
    name = Name(args[0])
    index = int(args[1])
    new_phone = Phone(args[2])
    rec = contacts.get(str(name))
    if rec:
        return rec.change_phone(index, new_phone)
    return f'There are no phones with name {name}'


COMMANDS = {help: 'help',
            add: 'add',
            exit: ['exit', 'close', 'good bye'],
            hello: 'hello',
            phone: 'phone',
            change: 'change',
            show_all: 'show all',
            }


def command_handler(text):
    for command, kword in COMMANDS.items():
        if isinstance(kword, str):
            if text.lower().startswith(kword):
                return command, text.replace(kword, '').strip().split()
        elif isinstance(kword, list):
            if text.strip().lower() in kword:
                return command, None
    return no_command, None


def main():
    print(help())
    while True:
        user_input = input('>>>')
        command, data = command_handler(user_input)

        print(command(*data))

        if command == exit:
            break


if __name__ == '__main__':
    main()
