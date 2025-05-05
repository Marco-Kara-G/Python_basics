name= "Marco"           #string
age= 25                 #int
height= 1.92            #float       
is_student= True        #boolean

# now we print the variables
print(name+ age + height + is_student) # this will not work because we are trying to add different types of variables

# we can use the str() function to convert the variables to string
print(str(name) + str(age) + str(height) + str(is_student)) # this will work because we are converting the variables to string


