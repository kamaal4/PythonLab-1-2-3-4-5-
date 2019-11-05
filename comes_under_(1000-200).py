def check_range():
    if(number >= 1000 and number <= 2000):
        print("True")
    else:
        print("False")
while 1:
    input_value = input("Enter a number and check it comes under 1000 to 2000 :")
    try:
        number = float(input_value)
        check_range()
        break
    except ValueError:
            print("Enter digits only.")
            continue
