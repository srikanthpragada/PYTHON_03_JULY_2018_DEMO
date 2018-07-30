with open(r"e:\classroom\python\phones.txt", "rt") as f:
    directory = {}
    for line in f.readlines():
        parts = line.split(':')
        if len(parts) >= 2:
            name = parts[0]
            phone = parts[1].strip("\n")
            if name in directory:
                directory[name].add(phone)  #add new number to existing set
            else:
                phones = set()
                phones.add(phone)
                directory[name] = phones    #Creating a new entry with name and set

    for name in sorted(directory.keys()):
        print("%-15s" % (name),end=': ')
        for phone in directory[name]:
            print(phone, end=' ')

        print()    # come to next line
