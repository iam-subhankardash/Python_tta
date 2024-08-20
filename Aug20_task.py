# Task-6
given_num = int(input("The given number is:"))
square_root = given_num**2    # pow(given_num,2)
cube_root = given_num**3      # pow(given_num,3)
print(square_root)
print(cube_root)

# Task-7
Year = int(input("Enter the Year: "))
if Year % 400 == 0 or Year % 100 != 0 and Year % 4 == 0:
    print("Yes! This Year is a leap Year")
else:
    print("This Year is not a leap Year")

# Task-8
## Let's assume x,y,z are 3 sides of a triangle.

x = int(input("The x side value is :"))
y = int(input("The y side value is :"))
z = int(input("The z side value is :"))

if (x == y and x != z) or (y == z and y != x) or (x == z and x != y):
    print("This is an isosceles triangle")
elif x == y and x == z and y ==z:
    print("This is an equilateral triangle")
else:
    print("This is an scalene triangle")

# Task-9
for i in range(1,101):
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)
