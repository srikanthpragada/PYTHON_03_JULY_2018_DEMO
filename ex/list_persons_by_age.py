from datetime import datetime, date, timedelta

f = open(r"e:\classroom\python\persons.txt")
persons = {}
for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue
    name = parts[0]
    try:
        dob = datetime.strptime(parts[1].strip("\n"), "%Y-%m-%d")
        td = datetime.now() - dob
        years = td.days // 365
        persons[name] = years  # add entry to dict
    except:
        pass

# sort dict by value and print key and value
for (n, a) in sorted(persons.items(), key=lambda t: t[1]):
    print(n, a)
