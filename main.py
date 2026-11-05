number1 = int(input("enter a number"))
number2 = int(input("enter a number"))
if number1>0 and number2>0:
    print ("both numbers are positive")
elif number1>0 or number2>0:
    print ("one of those are greater than 0")
else:
    print ("no number is greater than 0")