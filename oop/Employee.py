class Employee:
    hraper = 40

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print(self):
        print(self.name)
        print(self.salary)

    def get_salary(self):
        return self.salary + (self.salary * Employee.hraper / 100)


class Programmer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.lang = lang

    def print(self):
        super().print()
        print(self.lang)


e = Employee("Bob", 393933)
e.print()
p = Programmer("Scott", 693933, "Python")
p.print()
print( Programmer.__mro__)

