#if_else_example.py
"""
Example if statements using the various comparison operators.
"""

print("Enter two integers. Program will tell you the relationships they satisfy.")
a = int(input("Enter 1st integer: "))
b = int(input("Enter 2nd integer: "))

if a == b:
    print(a , "is equal to" , b)
# Should use else as two numbers are either equal or not, but wanted to show the != (not equal comparison operator)
elif a != b:
    print(a , "is not equal to" , b)
# In this program a or b can't be "None".  Adding this section to demonstrate the else
else:
    print(a , "or" , b , "must be null")

if a <= b:
    print(a , "is less than or equal to" , b)
    if a < b:
        print(a , "is less than" , b)

if a >= b:
    print(a , "is greater than or equal to" , b)
    if a > b:
        print(a , "is greater than" , b)

