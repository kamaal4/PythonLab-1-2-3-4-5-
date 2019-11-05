# Name: Mohd Mustafa Kamaal
# Roll no: 34
# Enrl no: A180571
# Batch: 1
#Q1. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

thislist =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Your list is\n",thislist)
while 1:
    address =input("Enter the location of element to delete it from the list :\n")
    try:
        input_address = int(address)
        if input_address == 0:
            thislist.remove('Red')
        elif input_address == 1:
            thislist.remove('Green')
        elif input_address == 2:
            thislist.remove('White')
        elif input_address == 3:
            thislist.remove('Black')
        elif input_address == 4:
            thislist.remove('Pink')
        elif input_address == 5:
            thislist.remove('Yellow')
        else:
            print("Please choose between 0 to 5")
        key = input("Enter 'e' to stop and print new list or to continue enter any key:")
        if key == 'e':
            print("New list is :",thislist)
            break
        else:
            continue
    except ValueError:
        print("Enter the location in integer only")
        continue
