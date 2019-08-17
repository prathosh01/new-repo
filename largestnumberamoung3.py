num1 = float(input("Enter the 1st number "))
num2 = float(input("enter the 2nd number "))
num3 = float(input("enter the 3rd number "))
if (num1>num2) and (num1>num3):
    largest = num1
elif (num2>num1) and (num2>num3):
    largest = num2
else:
    largest = num3
print("the greatest of 3 numbers is",largest)
