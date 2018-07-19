
try:
    num = int (input("Enter a number :"))
    # process
    print( 100 / num)
except ValueError as ex:
    print('Sorry! Invalid Input!', ex)
else:
    print("Done")
finally:
    print("The End!")

