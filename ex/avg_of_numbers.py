total = count = 0
for i in range(1, 11):
    try:
        num = int(input("Enter a number :"))
        total += num
        count += 1
    except:
        pass

print("Average : ", total / count)
