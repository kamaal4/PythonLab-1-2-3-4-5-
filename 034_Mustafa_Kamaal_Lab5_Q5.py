#Name :       Mohd. Mustafa kamaal
#Roll no.:    18BTCS034HY
#Enrl no.:    A180571
#Write a Python program to remove an item from a set if it is present in the set
this_set = set([1, 3, 4, 5])
print(this_set," is given set.")
rem = int(input("Enter element to remove from given set :"))
this_set.discard(rem)
print(this_set)
