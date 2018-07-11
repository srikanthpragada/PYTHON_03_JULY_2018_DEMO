# Take names until end is entered and print them in sorted order
names=[]

while True:
    name = input("Enter a name :")
    if name == "end":
        break
    names.append(name)


for n in sorted(names):
    print(n)

