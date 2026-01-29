#pyton variabel
#variabel nama

myvar = "joni"
my_var = "joni"
_my_var = "joni"
myVar = "joni"
MYVAR = "joni"
myvar2 = "joni"

#camel case
myVariableName = "John"

#pascal case
MyVariableName = "John"

#snake case
my_variable_name = "John"


#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python - Output Variables
x = "Python is awesome"
print(x)
###################
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#################
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#################
x = 5
y = 10
print(x + y)
#################
x = 5
y = "John"
print(x, y)

#Python - Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)