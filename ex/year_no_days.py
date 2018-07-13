years = {}
for y in range(1900, 2001):
    # years[y] = 366 if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 else 365
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        years[y] = 366
    else:
        years[y] = 365

print(years)

# List of tuples

years = []
for y in range(1900, 2001):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        years.append((y, 366))
    else:
        years.append((y, 365))

print(years)
