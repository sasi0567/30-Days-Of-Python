# Day 2: 30 Days of python programming
#Exercise 1
# Variables
first_name = "Sasidhar"
last_name = "Vakamalla"
full_name = first_name + " " + last_name
country = "India"
age = 18
root_two=1.414
is_dead = False
is_true = True
is_light_on = True

#Exercise 2
# Declaring Multiple variables on one line
a, b, c = 10, 20, 30

# Checking data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(root_two))
print(type(is_dead))
print(type(is_true))
print(type(is_light_on))
print(type(a))

# Comparing Length of first name
print("Length of first name is:", len(first_name))
print("Length of last name is:", len(last_name))

# Numbers 
num_one =int(input("First number: "))
num_two = int(input("Second number: "))

#Some Calculations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)
print("Exponent:", exp)
print("Floor Division:", floor_division)

# Circle calculations by taking input from the user
pi = 3.14159
radius = float(input("Enter radius: "))
area = pi * radius ** 2
print("Area of circle:", area)

# User input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)

# Python keywords
help("keywords")