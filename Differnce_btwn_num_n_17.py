#Name : Mohd Mustafa Kamaal
#Roll no: 34
#Enrl no: A180571
#Q:Write a Python program to get the difference between a given number(take input from the user) and 17, if the number is greater than 17 answers will be double the absolute difference.
while 1:
    input_value = input("Enter the number :")
    try:
        number = float(input_value)
        if number>17:
            difference = number-17
            result = difference*2
            print("Result is ",result)
            break
        else:
            difference = 17-number
            print("Result is ",difference)
            break
    except ValueError:
            print("Enter digits only.")
            continue
