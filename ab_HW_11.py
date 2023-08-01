from collections import UserDict
from datetime import date
from datetime import datetime

class BirthdayError(Exception):
    ...

class PhoneError(Exception):
    ...


def error_except(function):
    def inner(*args):
        try:
            function(*args)
        except BirthdayError:
            print('That is incorrect birthday!')
        except PhoneError as pe:
            if pe.args:
                print(f'This phone number is too {pe.args[0]}!')
                
            else:
                print('That is incorrect phone number!')
               
        except ValueError:
            print('Something is wrong!')
        except AttributeError:
            print('Something is wrong!')
        except KeyError:
            print('Name is incorrect!\n')
    return inner

class Field:
    def __init__(self, value) -> None:
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    def __str__(self) -> str:
        #print(self.value)
        return self.value
    
    def __repr__(self) -> str:
        if self != None:
            return str(self)
        else:
            return ""
        
    def __eq__(self, other):
        return self.value == other.value

class Name(Field):
    ...
    

class Phone(Field):
    # ...
    # def __init__(self):
    #     super().__init__()

    @property
    def value(self):
        return self.__value
    
    @value.setter
    @error_except
    def value(self, value):
        try:
            if (value.isdigit()) or (value.startswith('+') and int(value[1:].isdigit())):
                self.__value = value
                if 10 > len(value):
                    self.__value = None
                    raise PhoneError('short number')
                if 13 < len(value):
                    self.__value = None
                    raise PhoneError('long number')
            else:
                self.__value = None
        except ValueError:
            self.__value = None
            raise PhoneError

    def __str__(self):
        return str(self.value)

class Birthday(Field):

    def __init__(self, value: str) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, __new_value):
        d = date.fromisoformat(__new_value)
        if d:
            self.__value = d
        else:
            #raise ValueError("wrong date format, not ISO 8601")
            raise BirthdayError

    def __str__(self):
        return self.value.isoformat()
    
class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        # if birthday:
        self.birthday = birthday
        #print(self.phones)
    
    def add_phone(self, phone: Phone = None):
        #if phone.value not in [p.value for p in self.phones]:
        if phone not in self.phones:
            self.phones.append(phone)
            return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"
    
    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} change to {new_phone}"
        return f"{old_phone} not present in phones {self.name}"
    
    def del_phone(self, phone: Phone = None):
        i = 0
        result = ""
        for p in self.phones:
            if phone == p:
                self.phones.pop(i)
                result = f"{phone} delete phones {self.name}"
            i += 1
        if result == "":
            result = f"contact {self.name} have not phone {phone}"
        return result
    
    def days_to_birthday(self, birthday):
        date_now = datetime.now()
        days_in_year = 366 if (date_now.year+1)%4 == 0 else 365
        birthday_split = birthday.split('-')
        birthday_next = datetime(year=date_now.year+1, month=int(birthday_split[1]), day=int(birthday_split[2]))
        difference = birthday_next.date() - date_now.date()
        days_offset = difference.days
        days_offset = days_offset - days_in_year if days_offset > days_in_year else days_offset
        return days_offset

    def __str__(self) -> str:
        result = f"{self.name}: {', '.join(str(p) for p in self.phones) if self.phones else ''} {str(self.birthday) if self.birthday else ''}"
        return result
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
