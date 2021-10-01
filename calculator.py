# Program make a simple calculator

# This function adds two numbers
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

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
    return lcm

# This function finds the H.C.F of two numbers
def compute_hcf(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

# This function finds the exponent of a number
def compute_power(base, exponent):
    return pow(base, exponent)

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.LCM of 2 numbers")
print("6.HCF of 2 numbers")
print("7.Power")
print("0.Exit")

while True:
    # Take input from the user
    choice = input("Enter choice: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, " = ", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, " = ", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, " = ", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, " = ", divide(num1, num2))

        elif choice == '5':
            print("LCM of ", num1, " & ", num2, " = ", compute_lcm(num1, num2))

        elif choice == '6':
            print("HCF of ", num1, " & ", num2, " = ", compute_hcf(num1, num2))

        elif choice == '7':
            print(num1, "/", num2, "=", compute_power(num1, num2))            
            
    elif choice == '0':
        print('Thanks for using')
        break

    else:
        print("Invalid Input")
