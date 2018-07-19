class Account:
    # constructor
    def __init__(self, acno, customer, bal=0):
        # Object attributes
        self.__acno = acno
        self.customer = customer
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return "Acno : %d  Customer : %s  Balance : %d" % (self.__acno, self.customer, self.balance)


a1 = Account(1, "Mr. Gates")
a2 = Account(2, "Mr.Larry", 10000)
a1.deposit(10000)
a1.deposit(20000)

print(a1.customer, a1.balance)
print(a2)  # a2.__str__
print(str(a2))  # a2.__str__
