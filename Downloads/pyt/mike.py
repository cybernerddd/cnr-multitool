# for loop
#define the number of iterations
for i in range(5):
    #statement youre repeating
    print("i")
    print("--") #this isjust a separator


for something in range(3):
    print(something)

#while loop
seats = 5
while seats > 0:
    print("sell more tickets")
    seats = seats - 1

#if-else statements conditional statements
student = True
age = 13

if age >=13:
    print("You're free")
else:
    print("please play")

age = 16
if age > 12:
    print("applied disscount")
print("continue to checkout")

if age == 1:
    print("helow, wewlcome")
elif age == 16:
    print("on track")
else:
    print("get the fuk")

age = 160
is_student = False

if age < 18:
    if is_student == True:
        print("discount")
    else:
        print("sorry")
else:
    print("move to checkout")

#lists - theyre mutable (means they can be changed)
nums = [1,2,3,4,5]
nums[0] = 10
print(nums)

#products = ["apple", "banana", "orange"] #list of products
#choice = int(input()) #user input for the choice, and convert to integer
#print(products[choice]) #print the chosen product based on user input

#slicing
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[1:3]) #prints from index 1 to 2. starting index is inclusive, ending index is exclusive
print(letters[:4]) #prints from start to index 3

#functions (reusable blocks of code that perform a specific task)
print(1, "meme")
# print() and range() and input() are all built-in functions
#  Information to complete the task is passed as arguments to the function e.g: print(1, "meme") has two arguments 1 and "meme"

#The functions upper() and lower() allow you to quickly change the case of a string to all in uppercase or lowercase, respectively.
print("heLLo GhanA".upper())
# Functions that only work on certain objects (strings, lists, etc.) are called using dot . notation.
#.capitalize() function capitalizes the first letter of a string
print("hello ghana".capitalize())

# find() function checks if a character (or a pattern of characters) is present in a string
print("bee".find('e')) # returns 1, the index of the first occurrence of 'e'
# find() will return -1 if the value can't be found in the string.

#built-in list functions
# len() gives the length of a list. short for length. can be used on strings too
movie = "Avatar"
print(len(movie))
#len accepts all data types, so it doesnt use the .dot notation

# appent() adds an item to the end of a list. its called using dot notation because its specific to lists
fruits = ["apple", "banana"]
fruits.append("orange")

# insert() adds an item at to a list at a specific index or position
# takes two arguments, the index and the item to be added
fruits.insert(1, "grape") # inserts 'grape' at index 1
print(fruits)

# pop() removes an element from a list at a specified index and returns 
fruits.pop(2) # removes the item at index 2 ('banana')
print(fruits)

# custom functions
# funtion definition
def greet_user():
    print("hello from function") #function body, must be indented
    print("good day")
#function call
greet_user()

# A function might require arguments to complete its tasks. Arguments are put inside the parentheses () following the function name.
def greet(name):
    print("HELLO " + name)
greet("Mike")

#result of a function can be returned using the return statement.
def bmi(weight, height):
    bmi_value = weight / (height * height)
    return bmi_value # returns the calculated bmi value

# calling the bmi function and storing the result
patient_1 = bmi(70, 1.75) #stores the returned value in patient_1
print(patient_1)

# A function can return multiple values.
def calculate(a, b):
    sum_value = a + b
    diff_value = a - b
    return sum_value, diff_value
total, difference = calculate(10, 5)
print(total)
print(difference)


# Python allows function arguments to have default values. If the function is called without the argument, the argument gets its default value
def greet(name="Guest"):
    print("Welcome, " + name)
greet() # uses default value "Guest". They make arguments optional
greet("Alice") # uses provided value "Alice"

# tuples
# use () parentheses to define a tuple
coordinates = (10.0, 20.0)
print(coordinates[0]) # access first element
# tuples are immutable, meaning their elements cannot be changed after creation
scores = (90, 85, 90, 88)
print(scores.count(90)) # returns 2, the number of times 90 appears in the tuple

# max() and min() functions can be used to find the highest and lowest values in a collection
#tuple unpacking allows you to assign each element of a tuple to a separate variable in a single line of code
point = (3, 4)
x, y = point
print(x) # prints 3
print(y) # prints 4

# the * operator can be used when unpacking and dont know the number of elements in advance.Used to gather remaining elements of tuples into a list
data = (1, 2, 3, 4, 5)
a, b, *rest = data
print(a)    # prints 1
print(rest) # prints [3, 4, 5]

# sets - unordered collections of unique elements, creates using {} curly braces
colors = {"red", "green", "blue"}
# sets cant have duplicate elements, it wont throw an error but will ignore duplicates
# theyre mutable, use the add() and remove() methods to modify sets, with arguments passed inside the parentheses. using the dot notation.
# clear() funtion removes all elements from a set, and dont require any arguments
colors.add("yellow")
colors.remove("green")

# union() method combines two sets, returning a new set with all unique elements from both sets
set1 = {1, 2, 3}
set2 = {2, 4, 5}
combined_set = set1.union(set2) # union() takes another set as an argument
print(combined_set)

# dictionaries - key-value pairs, defined using {} curly braces
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# we access values using their keys inside square brackets []
print(person["name"]) # prints "Alice"
# or u can use the get() function. which is called using dot notation
person.get("name")

# you can get all the values and keys of a dictionary using the values() and keys() methods, respectively
info_keys = person.keys()
info_values = person.values()
print(info_keys)
print(info_values)

# the items() function prints all key-value pairs in a dictionary as tuples inside a list
info_items = person.items()
print(info_items)

nums = [x*2 for x in range(10)] #list comprehension
print(nums)

tags = ["python", "development", "tutorial"]

hashtags = ["#" + x for x in tags] # it takes expression, item and iterable
print(hashtags)

sports = ["soccer", "racket", "tennis", "cricket", "Baseball", "Basketball"]
first_sports = [x for x in sports if x[1] == 'r'] #conditional list comprehension
print(first_sports)

data = ["anna", "bob", "mery"]
names = [x.upper() for x in data]
print(names)

#buGS and errors
#Bugs are mistakes that may not interrupt execution but can cause incorrect behavior
#Exceptions are errors that occur during execution and disrupt the program's flow
#There are various types of exceptions. they can be predicted and handled using try-except blocks
prices = [10, 20, "200", 30]
try:
    #block of code that may raise an exception
    total = sum(prices)
    print("Total price:", total)
except TypeError:
    #code to handle the exception
    print("Error, theres a type shit")


#errors include syntax errors, name errors, index errors, key errors, and value errors
# you can have multiple except blocks to handle different types of exceptions
# to catch any exception regardless of its type, you can use a general except block without specifying an exception type
# finally block is used to define a block of code that will always execute, regardless of whether an exception occurred or not
proce = [10, 20, 30, "N/A", 50]
try:
    print(sum(proce))
except TypeError:
    print("check the proce list for non-numeric values")
finally:
    print("Need help? Contact support.")

# ELSE block can be used after all except blocks. It runs if no exceptions were raised in the try block
books = ["Book A", "Book B", "Book C"]
try:
    choice = int(input("Enter book index: "))
except IndexError:
    print("Index out of range")
else:
    print(books[choice] + " is a great choice!")

# raise statement allows you to manually trigger exceptions in your code
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print("Valid age:", age)

#lambda functions are small anonymous functions defined using the lambda keyword. can take multiple arguments separated by commas but can only have one expression
#lambda <arguments>: <expression>
#defined by using the lambda keyword, followed by the arguments, a colon and the expression to preform
lambda name: "Hello, " + name

#map() function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator)
# it takes two arguments: the function to apply and the iterable to process
mapped_names = map(lambda name: name.upper(), ["alice", "bob", "charlie"])
print(list(mapped_names))
#syntax: map(function, iterable)
# ✔ applies the function to every item
# ✔ returns a map object → convert with list()


# filter() function constructs an iterator from elements of an iterable for which a function returns true
# it also takes two arguments: the function to apply and the iterable to filter
filtered_numbers = list(filter(lambda x: x % 2 == 0, range(10)))
print(filtered_numbers)
#syntax: filter(function, iterable)
# ✔ keeps only items where function returns True
# ✔ also returns a filter object → convert to list

#args and kwargs
# *args allows a function to accept any number of positional arguments
def add_numbers(*args):
    total = 0
    for x in args:
        total += x
    return total

print(add_numbers(1, 2, 3, 4)) # returns 10
# you use *args when you dont know how many arguments the user will pass to your function or give

# **kwargs allows a function to accept any number of keyword arguments (arguments passed by name)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "->", value)
print_info(name="Alice", age=30, city="New York")
# you use **kwargs when you want to handle named arguments that you have not defined in advance


# decorators are a way to modify or enhance the behavior of functions or methods without changing their actual code
# You can apply a decorator to a function using the @ sign.
def uppercase(func):
    def wrapper():
        orig_result = func()
        modified_result = orig_result.upper()
        return modified_result
    return wrapper
# applying the decorator to the greet function
@uppercase
def greet():
    return "hello there"

# calling the decorated function
print(greet()) # prints "HELLO THERE"

#classes and objects
# A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.
class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    # method(function) inside a class
    def hack(self, target):
        print(f"{self.brand} is in {target}")

cybernerddd = car("Royce", "blue") #create an object of the class car


cybernerddd.hack("Accra target") #calling the hack method on the object
print(cybernerddd.color) #accessing the color attribute of the object

#they can also inherit attributes and methods from other classes
#parent class
class Animal:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def speak(self):
        print("Animal sound")

#child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, brand, breed, age):
       # initialize attributes of the superclass
        super().__init__(name, brand) 
        # additional attributes for Dog class
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")
# create an object of the Dog class
my_dog = Dog("Buddy", "Canine", "Labrador", 3)
my_dog.bark() #calling the bark method





