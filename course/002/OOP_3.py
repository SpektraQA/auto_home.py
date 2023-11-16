# class Employee:
#
#     raise_amount = 1.04
#
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#         self.salary = salary
#         self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
#
#     @property
#
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @full_name.setter
#     def full_name(self, name):
#         first_name, last_name = name.split()
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @full_name.deleter
#     def full_name(self):
#         self.first_name = None
#         self.last_name = None
#
#
#     def raise_salary(self):
#         self.salary = self.salary * Employee.raise_amount
#
#     def __str__(self):
#         return f'{self.full_name}'
#     def __repr__(self):
#         return f'Employee({self.first_name}, {self.last_name}, {self.salary})'
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
#     def __len__(self):
#         return len(self.full_name) - 1
#
#
# emp1 = Employee('Jack', 'Smith', 2000)
# emp2 = Employee('Mary', 'Smitt', 3000)
#
#
# emp1.full_name = 'Bob Green'
# del emp1.full_name
# print(emp1.full_name)
#
#
#
#
#
# # print(emp1)
# # print(repr(emp1))
# # print(emp1 + emp2)
# # print(len(emp1))


class Car:
    def __init__(self, make, model, color):
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def make(self):
        return self.__make

honda = Car('Honda', 'Civic', 'red')
print(honda.make)