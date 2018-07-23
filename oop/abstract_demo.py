from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def print(self):
        pass


class Programmer(Person):
    def print(self):
        pass


class Player(Person):
    def print(self):
        pass


# p = Person()
prog = Programmer()
