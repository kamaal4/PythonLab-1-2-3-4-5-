# Name: Mohd Mustafa Kamaal
# Roll no: 34
# Enrl no: A180571
# Batch: 1
import math
while 1:
    input_val = input("Enter radius to get the area of circle :")
#check if input_val matches the number, then calculate the area. else throw the error
    try:
        radius = float(input_val)
        area = (math.pi)*(radius*radius)
        print("Area of circle is",area)
        break
    except ValueError:
        print("Enter radius in digits only.")
        continue
