from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        # Перевіряємо, чи переданий номер телефону є рядком, має довжину 10 символів
        # та складається лише з цифр
        if not isinstance(value, str) or len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be a string of 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        # Ініціалізуємо ім'я запису та список телефонних номерів
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додаємо новий телефонний номер до запису
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Видаляємо вказаний телефонний номер із запису
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Перевіряємо, чи існує старий номер телефону для редагування
        if not self.find_phone(old_phone):
            raise ValueError("Phone number to edit does not exist")
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        # Шукаємо телефонний номер у записі та повертаємо його об'єкт,
        # якщо знайдено, або None, якщо номер відсутній
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        # Повертаємо рядок, який представляє дані запису
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        # Додаємо новий запис до адресної книги
        self.data[record.name.value] = record

    def find(self, name):
        # Знаходимо запис у книзі за іменем та повертаємо його,
        return self.data.get(name)

    def delete(self, name):
        # Видаляємо запис із адресної книги за іменем
        if name in self.data:
            del self.data[name]

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")