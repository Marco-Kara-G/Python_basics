# To print in python u must use the print() function.
# The print() function takes one or more arguments and prints them to the console.

print ("Hello marco, let's test the code")

# when u have to print variables u must look at the type of the variable.
# if the variable is a string, u can print it directly.

name= "marco"
print(name)

#OR

print("Hello " + name)
# In this case the console will print "Hello marco" without any type errors

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# if the variable is an int or a boolean, u cannot print it directly, u first need to convert it into a string.

age= 30
print ("you're " + str(age) + " years old")
# In this case the console will print "you're 30 years old" without any type errors

#u can also use the f-string method to print variables in python, u have to put the letter f before the string and use curly braces to insert the variable inside the string.

height= 1.92
print(f"Hello {name}, we know u are {age} years old and your height is {height} m")
# In this case the console will print "Hello marco, we know u are 30 years old and your height is 1.92 m" without any type errors

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------