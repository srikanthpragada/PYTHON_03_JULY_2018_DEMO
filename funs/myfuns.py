if __name__ == "__main__":  # module is run as script
    print("Invoking module!")
    print("Name : " , __name__)
else:  # module is being imported
    print("Importing module!")


def add(n1, n2):
    return n1 + n2


def iseven(n):
    return n % 2 == 0


