names = ['Larry', 'Bill', 'Joe','Kim']

for n in sorted(names, key=lambda n: len(n)):
    print(n)


for n in sorted(names, key=len):
    print(n)

