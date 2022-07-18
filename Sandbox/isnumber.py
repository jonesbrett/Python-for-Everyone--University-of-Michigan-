def ifnumeric(String1):
    try:
        float(String1)
        return True
    except:
        print("This is not a numeric value")


String1 = input("Please enter a number: ")
if ifnumeric(String1) == True:
    print("You entered the number ", String1)
