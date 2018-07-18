
try:
    num = int (input("Enter a number :"))
    # process
    print( 100 / num)
except ValueError:
    print('Sorry! Invalid Input!')
finally:
    print("The End!")

