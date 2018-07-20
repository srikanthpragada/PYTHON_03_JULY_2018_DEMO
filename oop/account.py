class Account:
    # class attributes
    minbal = 5000

    # constructor
    def __init__(self, acno, customer, bal=0):
        # Object attributes
        self.acno = acno
        self.customer = customer
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return "Acno : %d  Customer : %s  Balance : %d" % (self.acno, self.customer, self.balance)

    def __eq__(self, other):
        print("__eq__")
        return self.acno == other.acno

    def __ge__(self, other):
        return self.balance >= other.balance


a1 = Account(1, "Mr. Gates", 50000)
a2 = Account(1, "Mr. Gates", 50000)
print(a1 != a2)
print(a1 >= a2)
