from AddressBook import *


class Bot:

    def __init__(self):
        self.book = AddressBook()
        self.operations = {
            "add": self.add,
            "search": self.search,
            "edit": self.edit,
            "remove": self.remove,
            "save": self.save,
            "load": self.load,
            "congratulate": self.congratulate,
            "view": self.view,
            "exit": self.exit,
            "help": self.help
        }

    def add(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        self.book.add(record)
        self.book.save("auto_save")

    def search(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (self.book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)

    def edit(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        self.book.edit(contact_name, parameter, new_value)
        self.book.save("auto_save")

    def remove(self):
        pattern = input("Remove (contact name or phone): ")
        self.book.remove(pattern)
        self.book.save("auto_save")

    def save(self):
        file_name = input("File name: ")
        self.book.save(file_name)

    def load(self):
        file_name = input("File name: ")
        self.book.load(file_name)

    def congratulate(self):
        print(self.book.congratulate())

    def view(self):
        print(self.book)

    def exit(self):
        print("Good bye!")
        return True

    def try_again(self):
        print("there no such command, try again")

    def help(self):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in self.operations.keys():
            print(format_str.format(command))
        action = input().strip().lower()
        self.handle(action)

    def handle(self, action):
        self.operations.get(action, self.try_again)()

    # def handle(self, action):
    #     if action == 'add':
    #         name = Name(input("Name: ")).value.strip()
    #         phones = Phone().value
    #         birth = Birthday().value
    #         email = Email().value.strip()
    #         status = Status().value.strip()
    #         note = Note(input("Note: ")).value
    #         record = Record(name, phones, birth, email, status, note)
    #         return self.book.add(record)
    #     elif action == 'search':
    #         print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
    #         category = input('Search category: ')
    #         pattern = input('Search pattern: ')
    #         result = (self.book.search(pattern, category))
    #         for account in result:
    #             if account['birthday']:
    #                 birth = account['birthday'].strftime("%d/%m/%Y")
    #                 result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
    #                 print(result)
    #     elif action == 'edit':
    #         contact_name = input('Contact name: ')
    #         parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
    #         new_value = input("New Value: ")
    #         return self.book.edit(contact_name, parameter, new_value)
    #     elif action == 'remove':
    #         pattern = input("Remove (contact name or phone): ")
    #         return self.book.remove(pattern)
    #     elif action == 'save':
    #         file_name = input("File name: ")
    #         return self.book.save(file_name)
    #     elif action == 'load':
    #         file_name = input("File name: ")
    #         return self.book.load(file_name)
    #     elif action == 'congratulate':
    #         print(self.book.congratulate())
    #     elif action == 'view':
    #         print(self.book)
    #     elif action == 'exit':
    #         pass
    #     else:
    #         print("There is no such command!")
