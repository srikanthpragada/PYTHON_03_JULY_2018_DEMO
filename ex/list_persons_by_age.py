from datetime import datetime, date, timedelta

f = open(r"e:\classroom\python\persons.txt")
persons = {}
for line in f.readlines():
    parts = line.split(",")
    # print(parts[1])
    dob = datetime.strptime(parts[1].strip("\n"), "%Y-%m-%d")
    td = datetime.now() - dob
    years = td.days // 365
    persons[parts[0]] = years

# sort dict by value and print key and value


