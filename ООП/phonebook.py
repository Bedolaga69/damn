class Phonebook:
    def __init__(self, contacts=None, **kwargs):
        if contacts is None:
            contacts = {}
        if contacts:
            self.contacts = contacts
        else:
            self.contacts = kwargs


    def add_contacts(self, name, phone_number):
        if name in self.contacts.keys():
            print("контакт уже существует")
        else:
            self.contacts[name] = phone_number
            print("контакт добавлен")


    def find_p_number(self, name):
        return self.contacts.get(name, f"контакт {name} не найден")


    def delete_contacts(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"контакт {name} удален")
            return True
        else:
            print(f"контакт {name} не найден")
            return False


    def show_all_contacts(self):
        if not self.contacts:
            print("телефонная книга пуста")
        else:
            print("все контакты:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")


    def update_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            print(f"контакт {name} успешно обновлен")
        else:
            print(f"контакт {name} не найден")



pb = Phonebook(андрей="123-4567", боб="987-6543")
pb.add_contacts("мистер бист", "555-1234")
pb.show_all_contacts()
pb.update_contact("андрей", "111-2222")
pb.delete_contacts("боб")
print(f"номер андрея {pb.find_p_number('андрей')}")
pb.show_all_contacts()


# def print_pets(**kwargs):
#     print(kwargs)
#     for pet, name in kwargs.items():
#         print(f"{pet}: {name}")
#
#
# print_pets(собака = "дружок", fsd = "s")
# print_pets()










# class Phonebook:
#     def __init__(self, contacts=None, **kwargs):
#         if contacts is None:
#             contacts = {}
#         if contacts:
#             self.contacts = contacts
#         else:
#             self.contacts = kwargs
#
#
#     def add_contacts(self, name, phone_number):
#         if name in self.contacts.keys():
#             print("контакт уже существует")
#         else:
#             self.contacts[name] = phone_number
#             print("контакт добавлен")
#
#
#     def find_p_number(self, name):
#         return self.contacts.get(name, f"контакт {name} не найден")
#
#
#     # def delete_contacts(self, name):
