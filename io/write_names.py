with open(r"e:\classroom\python\names.txt", "wt") as f:
    names = ["Python", "C#", "Java", "JavaScript", "C++"]
    for name in names:
        f.write(name + "\n")

