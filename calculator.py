# Program for a simple calculator

import decimal
import math

# Adds two numbers
def add(x, y):
    return x + y

# Subtracts two numbers
def subtract(x, y):
    return x - y

# Multiplies two numbers
def multiply(x, y):
    return x * y

# Divides two numbers
def divide(x, y):
    if y != 0:
        return x / y 
    else:
        return 'denominator can not be zero'

# Calculates the L.C.M. of two input number
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
    # the math.lcm() function will give the same answer with less lines of code
    # example: 
    #   import math
    #   print(math.lcm(2,3,4)) [find the the least common multiple of the integers]

# Calculates the H.C.F of two numbers
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
    # the math.gcd() function will give the same answer with less lines of code
    # example: 
    #   import math
    #   print(math.gcd(12,18)) [find the the greatest common divisor(also called The Highest Common Factor) of the two integers]

# Calculates the exponent of a number
def compute_power(base, exponent):
    base = float(base)
    # return pow(base, exponent)
    answer = 1
    if(exponent == None):
        return base ** 0.5

    else:
        if(exponent<0):
            positiveExponent=exponent*-1
            return 1/(base**positiveExponent)
        else:
            while exponent > 0:
                answer = base * answer
                exponent -= 1
            return answer
    # the math.pow() function will give the same answer with less lines of code
    # example: 
    #   import math
    #   print(math.pow(9, 3))  [Return the value of 9 raised to the power of 3]

# Calculates the area of a circle
def area_of_circle(radius):
    return math.pi * compute_power(radius, 2)

# Calculates the circumference of a circle
def circumference_of_circle(radius):
    return 2 * math.pi * radius

# Convert a value from radian to degree
def radian_to_degree(radian):
    return radian * (180/math.pi)
    # the math.degrees() function will give the same answer in a simpler way
    # examples:
    #   import math
    
    #   print (math.degrees(math.pi / 180))
    #   print (math.degrees(180))
    #   print (math.degrees(1))

# Convert a value from degree to radian
def degree_to_radian(degree):
    return degree * (math.pi/180)
    # the math.radians() function will give the same answer in a simpler way
    # examples:
    #   import math

    #   print (math.radians(180 / math.pi))
    #   print (math.radians(180))
    #   print (math.radians(1))

# Find the value of x using Sine, Cosine or Tangent
def find_x_with_sin_cos_tan(opposite, hypotenuse, adjacent, angle):
    print(type(hypotenuse) is str)
    if opposite != 'x' and opposite != '': opposite = float(opposite)
    if hypotenuse != 'x' and hypotenuse != '': hypotenuse = float(hypotenuse)
    if adjacent != 'x' and adjacent != '': adjacent = float(adjacent)
    if angle != 'x' and angle != '': angle = float(angle)
    # soh
    if adjacent == '':
        # opp = hyp*sinZ
        if opposite == 'x':
            return hypotenuse * (math.sin(angle))
        # hyp = opp/sinZ
        if hypotenuse == 'x':
            return opposite/(math.sin(angle))
        # ang = sin(opp/hyp)
        if angle == 'x':
            return (math.sine(opposite/hypotenuse))

    # cah
    if opposite == '':
        # adj = hyp*cosZ
        if adjacent == 'x':
            return hypotenuse * (math.cos(angle))
        # hyp = adj/cosZ
        if hypotenuse == 'x':
            return adjacent/(math.cos(angle))
        # ang = cos(adj/hyp)
        if angle == 'x':
            return (math.cos(adjacent/hypotenuse))

    # toa
    if hypotenuse == '':
        # opp = adj*tanZ
        if opposite == 'x':
            return adjacent * (math.tan(angle))
        # adj = opp/tanZ
        if adjacent == 'x':
            return opposite/(math.tan(angle))
        # ang = tan(opp/adj)
        if angle == 'x':
            return (math.tan(opposite/adjacent))

    # angle
    if angle == '':
        print('No angle was given.\nPythagoras therom will be used to find the length of a missing side.')
        return pythagoras_theorem(opposite, hypotenuse, adjacent)
        # math.sin(), math.cos() and math.tan() can be used to make thwese calculations in a simpler way and using less code
        # examples of how math. can be used:
        #   Sine:
        #       math.sin(math.pi / 2) [Out: 1.0]
        #       math.sin(math.radians(90))   # Sine of 90 degrees [Out: 1.0]
        #   arc sine:
        #       math.asin(1) [Out: 1.5707963267948966  (= pi / 2)]
        #       math.asin(1) / math.pi [Out: 0.5]

        #   Cosine:
        #       math.cos(math.pi / 2) [Out: 6.123233995736766e-17 ]
        #           Almost zero but not exactly because "pi" is a float with limited precision!
        #   arc cosine:
        #       math.acos(1) [Out: 0.0]

        #   Tangent:
        #       math.tan(math.pi/2) [Out: 1.633123935319537e+16 ]
        #           Very large but not exactly "Inf" because "pi" is a float with limited precision
        #   arc tangent:
        #       math.atan(math.inf) [Out: 1.5707963267948966 # This is just "pi / 2"]
        #       math.atan(float('inf')) [Out: 1.5707963267948966 # This is just "pi / 2"]

# find the length of a side using pythagoras theorem
def pythagoras_theorem(sideA, hypotenuse, sideB):
    if hypotenuse == 'x':
        return square_root(compute_power(sideA, 2) + compute_power(sideB, 2))

    if sideA == 'x':
        return square_root(compute_power(hypotenuse, 2) - compute_power(sideB, 2))
        
    if sideB == 'x':
        return square_root(compute_power(hypotenuse, 2) - compute_power(sideA, 2))
        # the math.hypot() function will give the same answer with less lines of code
        # example: 
        #   import math
        #   print(math.hypot(2, 4))  [Return the value of SquareRoot(2**2 + 4**2)]

def square_root(number):
    return compute_power(number, None)
    # the math.sqrt() function will give the same answer with less lines of code
    # example:
    #   import math
    #   print (math.sqrt(9)) [Return the square root of 9]
        
def area_of_triangle(sideA, sideB, sideC):
    # calculate the semi-perimeter  
    semiPerimeter = (sideA + sideB + sideC) / 2  

    # calculate the area  
    return (semiPerimeter*(semiPerimeter-sideA)*(semiPerimeter-sideB)*(semiPerimeter-sideC)) ** 0.5  


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.LCM of 2 numbers")
print("6.HCF of 2 numbers")
print("7.Power")
print("8.Square root")
print("9.Circle's Area")
print("10.Circle's Circumference")
print("11.Convert radian to degree")
print("12.Convert degree to radian")
print("13.Find the value of X, using Sine, Cosine or Tangent")
print("14.Pythagoras theorem")
print("15.Area of a triangle")
print("0.Exit")

while True:
    # Take input from the user
    choice = input("\nEnter choice: ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15):

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
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            print(base, " to the power of ", exponent, " = ", compute_power(base, exponent))

        elif choice == '8':
            base = float(input("Enter the base: "))
            print("Square root of ", base, " = ", square_root(base))

        elif choice == '9':
            num1 = float(input("Enter the radius: "))
            print("Area of circle with radius ", num1, " is", area_of_circle(num1))

        elif choice == '10':
            num1 = float(input("Enter the radius: "))
            print("Circumference of circle with radius", num1, "is", circumference_of_circle(num1))

        elif choice == '11':
            num1 = float(input("Enter a number in radians: "))
            print("Radian value of", num1, " in decimal is", radian_to_degree(num1))

        elif choice == '12':
            num1 = float(input("Enter a number in degrees: "))
            print("Degree value of", num1, " in radians is", degree_to_radian(num1))

        elif choice == '13':
            print("for the value to be found, enter a lowercase 'x' without the quotes.")
            print("for the value that is not needed to be found, leave it blank.")
            opposite = (input("Length of opposite side: "))
            hypotenuse = (input("Length of hypotenuse side: "))
            adjacent = (input("Length of adjacent side: "))
            angle = (input("Angle in degrees: "))
            print("The value of X is", find_x_with_sin_cos_tan(opposite, hypotenuse, adjacent, angle))

        elif choice == '14':
            print("for the value to be found, enter a lowercase 'x' without the quotes.")
            opposite = (input("Length of side A: "))
            hypotenuse = (input("Length of hypotenuse side: "))
            adjacent = (input("Length of side B: "))
            print("The length of the missing side is", pythagoras_theorem(opposite, hypotenuse, adjacent))
                 
        elif choice == '15':
            sideA = (input("Length of side A: "))
            sideB = (input("Length of side B: "))
            sideC = (input("Length of side C: "))
            print("The area of the triangle is:", area_of_triangle(sideA, sideB, sideC))

    elif choice == '0':
        print('Thanks for using')
        break

    else:
        print("Invalid Input")
