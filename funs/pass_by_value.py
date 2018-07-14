def swap(n1, n2):
    print(id(n1))
    print(id(n2))
    n1, n2 = n2, n1
    print(id(n1))
    print(id(n2))


a = 10
b = 20
print(id(a))
print(id(b))
swap(a, b)
print(a, b)
