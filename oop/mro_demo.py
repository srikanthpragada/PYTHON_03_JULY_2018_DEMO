class A:
    def print(self):
        print("A")


class B(A):
    def print(self):
        print("B")


class C(A):
    def print(self):
        print("C")


class D(C,B):
    pass
#     # def print(self):
#     #     print("C")

obj = D()
print(D.__mro__)
obj.process()


