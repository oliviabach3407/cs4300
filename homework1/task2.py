'''
Create a Python script in Replit that demonstrates the use of various data types, including integers, floating-point numbers, strings, and booleans.
Implement a pytest test case for each data type, ensuring that the script's behavior matches the expected outcomes.
'''
#gets the data type of a variable and returns it as a string
def get_type(thing):
    #format is <class 'int'>"
    return str(type(thing))


#some sample data to use with different data types:
name = "John"
age = 25
height = 1.75
is_student = True

#print so can be tested through stdout
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
