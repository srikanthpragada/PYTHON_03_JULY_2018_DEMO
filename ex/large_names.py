names = ["larry", "Stephen", "bill", "Jackson"]

for n in filter(lambda n: len(n) > 5, names):
    print(n)


for n in sorted(names, key=str.upper):
    print(n)


for n in sorted(names, key=lambda n: n.upper()):
    print(n)
