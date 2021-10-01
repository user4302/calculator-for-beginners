# Program make a simple calculator

# This function adds two numbers
import decimal
import math


def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    if y != 0:
        return x / y  # denominator can't be zero
    else:
        return 'denominator can not be zero'


# This function finds the L.C.M. of two input number
def compute_lcm(x, y):
    # choose the greater number
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


# This function finds the H.C.F of two numbers
def compute_hcf(x, y):
    # validate decimal values
    hcf = 0
    dec_x = decimal.Decimal(str(x))
    dec_y = decimal.Decimal(str(y))

    dp_x = -(dec_x.as_tuple().exponent)
    dp_y = -(dec_y.as_tuple().exponent)

    if dp_x > dp_y:
        multiplier = int("1" + (dp_x * "0"))
    else:
        multiplier = int("1" + (dp_y * "0"))

    final_x = int(dec_x * multiplier)
    final_y = int(dec_y * multiplier)

    # choose the smaller number
    if final_x > final_y:
        smaller = final_y
    else:
        smaller = final_x
    for i in range(1, smaller + 1):
        if (final_x % i == 0) and (final_y % i == 0):
            hcf = i

    hcf = hcf / multiplier
    return hcf


# This function finds the exponent of a number
def compute_power(base, exponent):
    return pow(base, exponent)


def area_of_circle(radius):
    return math.pi * (compute_power(radius, 2))


def circumference_of_circle(radius):
    return 2 * math.pi * radius


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.LCM of 2 numbers")
print("6.HCF of 2 numbers")
print("7.Power")
print("8.Circle's Area")
print("9.Circle's Circumference")
print("0.Exit")

while True:
    # Take input from the user
    choice = input("\nEnter choice: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "+", num2, " = ", add(num1, num2))

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "-", num2, " = ", subtract(num1, num2))

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "*", num2, " = ", multiply(num1, num2))

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, "/", num2, " = ", divide(num1, num2))

        elif choice == '5':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("LCM of ", num1, " & ", num2, " = ", compute_lcm(num1, num2))

        elif choice == '6':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("HCF of ", num1, " & ", num2, " = ", compute_hcf(num1, num2))

        elif choice == '7':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(num1, " to the power of ", num2, " = ", compute_power(num1, num2))

        elif choice == '8':
            num1 = float(input("Enter the radius: "))
            print("Area of circle with radius ", num1, " is", area_of_circle(num1))

        elif choice == '9':
            num1 = float(input("Enter the radius: "))
            print("Circumference of circle with radius ", num1, " is", circumference_of_circle(num1))

    elif choice == '0':
        print('Thanks for using')
        break

    else:
        print("Invalid Input")
