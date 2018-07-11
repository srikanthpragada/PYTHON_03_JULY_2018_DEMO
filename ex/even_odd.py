odd_nums = []
even_nums = []
for i in range(1, 6):
    num = int(input("Enter a number :"))
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

print(odd_nums)
print(even_nums)
