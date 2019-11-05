def check_range():
    if(number > 1000 and number < 2000):
        print("Yes your Entered number (",number,")is lies under 1000 to 2000.")
    elif(number == 1000 or number == 2000):
        print("your Entered number (",number,") is equal to 1000 or 2000.")
    else:
        print("Your Entered number (",number, ") does not belongs to the range limit.")
while 1:
    input_value = input("Enter a number and check it comes under 1000 to 2000 :")
    try:
        number = float(input_value)
        check_range()
        break
    except ValueError:
            print("Enter digits only.")
            continue
