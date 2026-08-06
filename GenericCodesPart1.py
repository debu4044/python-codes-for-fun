# 1. Sphere and Cube Calculations
print("Sphere calculations:")
radius = float(input("Enter radius of sphere: "))
sphere_area = 4 * 3.14 * radius * radius
sphere_circumference = 2 * 3.14 * radius
sphere_volume = (4 / 3) * 3.14 * radius * radius * radius
print("Area:", sphere_area, "Circumference:", sphere_circumference, "Volume:", sphere_volume)

print("\nCube calculations:")
side = float(input("Enter side of cube: "))
cube_area = 6 * side * side
cube_perimeter = 12 * side
cube_volume = side * side * side
print("Area:", cube_area, "Perimeter:", cube_perimeter, "Volume:", cube_volume)

# 2. Print Even Numbers from List
numbers = input("Enter numbers separated by spaces: ").split()
even_numbers = []
for num in numbers:
    if int(num) % 2 == 0:
        even_numbers.append(num)
print("Even numbers:", even_numbers)

# 3. Print Positive Numbers from List
positive_numbers = []
for num in numbers:
    if int(num) > 0:
        positive_numbers.append(num)
print("Positive numbers:", positive_numbers)

# 4. Find Max or Min of Three Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Maximum:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Maximum:", num2)
else:
    print("Maximum:", num3)
if num1 <= num2 and num1 <= num3:
    print("Minimum:", num1)
elif num2 <= num1 and num2 <= num3:
    print("Minimum:", num2)
else:
    print("Minimum:", num3)

# 5. Quadratic Equation Roots
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("Roots are real and distinct:", root1, root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("Roots are real and equal:", root)
else:
    print("Roots are complex and cannot be calculated here.")

# 6. Character Classification
char = input("Enter a character: ")
if char.isalpha():
    if char.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif char.isdigit():
    print("Digit")
else:
    print("Special character")

# 7. Factorial of a Number
number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print("Factorial:", factorial)

# 8. Reverse 5-digit Number
number = int(input("Enter a number: "))
numtostring = str(number)
finalop = numtostring[::-1]
print(finalop)

# Reverse a 5-digit number
num = int(input("Enter a 5-digit number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print(f"Reversed number: {reverse}")

# 9. Count Alphabets and Digits
string = input("Enter a string: ")
alphabets = 0
digits = 0
for char in string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
print("Alphabets:", alphabets, "Digits:", digits)

# 10. Youngest of Three
age1 = int(input("Enter age of first person: "))
age2 = int(input("Enter age of second person: "))
age3 = int(input("Enter age of third person: "))
if age1 <= age2 and age1 <= age3:
    print("Youngest age:", age1)
elif age2 <= age1 and age2 <= age3:
    print("Youngest age:", age2)
else:
    print("Youngest age:", age3)
