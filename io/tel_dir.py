with open(r"e:\classroom\python\phones.txt", "rt") as f:
    directory = {}
    for line in f.readlines():
        parts = line.split(':')
        if len(parts) >= 2:
            directory[parts[0]] = parts[1].strip("\n")

    for name in sorted(directory.keys()):
        print("%-10s  %s" % (name,directory[name]))
