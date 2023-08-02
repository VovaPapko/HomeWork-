from HW_clas_12 import Name, Phone, Birthday, Record, AddressBook
address_book = AddressBook()
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"
        except ValueError:
            return "Incorrectly entered data!"
        except IndexError:
            return "Invalid command format"
    return wrapper
@input_error
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    birthday = None
    if len(args) == 3:
        birthday = Birthday(args[2])
    phone = Phone(args[1]) if len(args) > 1 else None
    birthday = Birthday(args[2]) if len(args) > 2 else None
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    rec = Record(name, phone, birthday)
    return address_book.add_record(rec)


@input_error
def change(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    birthday = None
    if len(args) == 4:
        birthday = Birthday(args[3])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact with name {name} in address book"
@input_error
def remove(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.remove_phone(phone)
    # else:
    return f"No contact with name {name} in address book"
def unknown(*args):
    return "Enter a new command"
def show_all(*args):
    if address_book.data:
        result = "list:\n"
        return result + "\n".join(str(r) for r in address_book.values())
    else:
        return "Empty list."
def hello(*args):
    return "How can I help you?"
def exit(*args):
    return "Good bye!"
COMMANDS = {
    hello: ("hello",),
    add: ("add", "+"),
    change: ("change", "зміни"),
    remove: ("remove",),
    show_all: ("show all",),
    exit: ("good bye", "close", "exit"),
}
@input_error
def parser(text: str):
    for cmd, keywords in COMMANDS.items():
        for keyword in keywords:
            if text.lower().startswith(keyword):
                data = text[len(keyword) :].strip().split()
                return cmd, data
    return unknown, []
def main():
    print("Welcome to the bot!")
    while True:
        user_input = input("Enter command: ")
        cmd, data = parser(user_input)
        result = cmd(*data)
        # result = cmd(*data)
        # print(result)
        if cmd == exit:
            # break
            address_book.save_to_file("address_book.pickle")
            print(cmd(*data))
            break
        result = cmd(*data)
        print(result)
if __name__ == "__main__":
    if address_book.load_from_file("address_book.pickle"):
        print("Restored from file")
    else:
        print("An address book has been created")
    main()
