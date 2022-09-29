# Create a basic function that will print a fun fact when it is called
def funfact():
    print("There are 63,360 inches in a mile!")


# Call the function
funfact()

# Create a function that takes in a number and prints out a statement
# about how the user has # projects to work on
def projects(num):
    print(f"You have {num} projects to work on!")


# Call the function twice, each time with a different value
projects(5)
projects(7)

# Create a function that takes in two parameters, an age and a name,
# and prints out a statement about how that person is # years old
def yearsold(age, name):
    print(f"{name} is {age} years old!")


# Call the function twice, each time with a different name and number
yearsold(24, "Mr. G")
yearsold(52, "Mr. G's Dad")

# Create a function that will take in an iterable holding several movies
# and print out a positive review of each of them using a loop
def moviereviews(movies):
    for movie in movies:
        print(f"{movie} is one of my favorite movies!")


# Create an iterable (list, tuple, or set) with at least 3 of your favorite
# movies as strings
favmovies = ("Star Wars", "Miracle", "Harry Potter")

# Call the function with your iterable
moviereviews(favmovies)

# Create a function that takes in a number to print out as an amount of money,
# and make the default value of the number 100
def money(amt=100):
    print(f"You have ${amt:,.2f}!")


# Call the function with an amount of money passed in and with nothing passed in
money(1000)
money()

# Create a function that takes in a current amount of money,
# and returns the money with an allowance added to it
def allowance(amt):
    return amt + 20


# Create a variable with an initial money value
cash = 30

# Print a statement about how much money you have after getting
# an allowance using your function
print(f"With my allowance I have ${allowance(cash):.2f}!")

# Try again with a different amount of money
print(f"With my allowance I have ${allowance(100):.2f}!")

# Create a function that takes in two boolean values and returns
# the result of the first *or* the second
def boolor(bool1, bool2):
    return bool1 or bool2


# Create two boolean variables
b1 = True
b2 = False

# Create a third boolean variable whose value is set to the function's
# output from your other two boolean variables. Then print out the new value
b3 = boolor(b1, b2)
print(b3)

# Create a function that takes in three numbers, and returns the larger of:
# The three numbers multiplied together
# The first number, raised to the second number (exponent), minus the third number
def larger(num1, num2, num3):
    mult = num1 * num2 * num3
    other = num1**num2 - num3
    if mult > other:
        return mult
    else:
        return other


# Call the function twice, with different sets of values and print the results
print(larger(2, 3, 4))
print(larger(4, 5, 1))

# Create a function that takes in two numbers and returns
# the minimum (the smaller of the two)
def min(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2


# Test it out on two pairs of numbers and print the results
print(min(5, 10))
print(min(15, 3))

# Create a function that takes in a list of numbers and use a
# loop to add them all up and then return the result
def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total


# Create two lists of numbers, each having at least 3
nums1 = [23, 45, 72, 34]
nums2 = [112, 234, 987]

# Call the function on both of these lists and print the results
print(sum(nums1))
print(sum(nums2))

# Create a function that takes in a list of names and use a loop
# to go through and greet each name individually. Have it print a
# unique greeting for a specific name you choose, and a normal greeting
# for all the others
def greet(names):
    for name in names:
        if name == "Jeet":
            print("Yo Jeet what's up!")
        else:
            print(f"Hi {name}!")


# Create two lists of names. Both will be made up of names of students,
# but only one list should contain the special name you chose
names1 = ["Madeline", "Naomi", "Evan", "Gage", "Jeet"]
names2 = ["Jayvion", "Khamani", "Micah", "Damario", "Josiah"]

# Call the function on both of your lists
greet(names1)
greet(names2)
