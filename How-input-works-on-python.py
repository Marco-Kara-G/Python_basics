# This program demonstrates how to take input from the user in Python.
# It uses the input() function to get data from the user and then prints a message using that data.

name= input("Enter your name: ")
age= input("Enter your age: ")

# The input() function takes a string as an argument, which is displayed to the user as a prompt.

print("Hello " + name + ", you are " + age + " years old.")

# in this case we dont need to convert the input to an int or string because the input() function already returns a string.



#if u want to convert variables in other data tyoe, u must use other function

newAge= int(age) + 1
print("Next year you will be " + str(newAge) + " years old.")

# In this case, we convert the age to an integer using int() and then add 1 to it.

# we can also create a boolean variable from input variables

isAdult= newAge >= 18
print("Are you an adult? " + str(isAdult))

