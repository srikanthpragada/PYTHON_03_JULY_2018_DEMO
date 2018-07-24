with open(r"e:\classroom\python\names.txt", "rt") as f:
    lines = f.readlines()
    for name in lines:
        print(name, end='')

    print("Reversed Files")
    for name in reversed(lines):
        print(name, end='')