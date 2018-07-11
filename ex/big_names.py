# Take names until end is entered and print them in sorted order
names=[]
total = 0
for i in range(1,6):
    name = input("Enter a name :")
    names.append(name)
    total +=  len(name)

# Calculate avg length
avg = total // 5

for n in names:
    if len(n) > avg:
        print(n)

