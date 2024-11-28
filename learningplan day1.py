#implicit conversion
# as according to this the implicit conversion automatically converts integer into float because while adding the int to float or float to int the result always stores in float value 

"""a=10
b=10.2
result=a+b
print(result)
print(type(result))"""


#explicit function 
#in this the programmer have to manually define it 
#Explicit conversion requires the use of built-in functions to convert data types. Here are some examples of explicit type conversion:
"""a=10
b=int(a)

print(a)
print(type(a))"""

###################################################################################################################################################

#write a conditional statement 

#in this code we have assigned the input value to num variable then the condition checks that if the number is greater than 0 its a positive number 
# and if it is less than 0 it is negative number and if it is 0 then it is a wrong input beacuse we have just assigned the condition that number is
# greater than or less then 0 if we want to include 0 also we can write llike num>=0 or num<=0

"""num = float(input("Enter a number: "))
if num >0:
    print("It is a positive number")
elif num<0:
    print("It is a negative number")
else:
    print("wrong input")"""

####################################################################################################################################################

#How do you define a function with default parameters?

#as assiging the default values to the default parameter as if user does not provide any input so this default values automatically called 
"""def calculate_area(width=5, height=10):
    area = width * height
    return area"""

#as here we r calling the function with default parameter
"""area1 = calculate_area()
print(f"Area with default parameters: {area1}")"""

#as here if user provides only one input so the second input called by default
"""area2 = calculate_area(width=7)
print(f"Area with width 7 and default height: {area2}")"""

#as here the user providing both the inputs
"""area3 = calculate_area(width=3, height=4)
print(f"Area with width 3 and height 4: {area3}")"""

#################################################################################################################################################

#Create a list comprehension to generate a list of squares for numbers from 1 to 10.

#the list comprehension is the method to write the loop condition in one line which helps to write the clean and understable code
#in this square we r taking a variable in which we r using x**2 to calculate the square and for the loop we have provide the range 1 to 11 
# means from the iteration begins from 1 to 10 and this will iterate each number 

"""squares = [x**2 for x in range(1, 11)]

#here we are printing the data which gets stored in sqaure 
print(squares)"""

####################################################################################################################################

#How can you add and remove elements from a set?
#as in this we have assigned 4 elements to the set and then performed remove method on this 
#also we can use add(),discard(),update() method on it. 

"""my_set={1,2,3,4}
my_set.remove(4)
print(my_set)"""

########################################################################################################################################

#Demonstrate the use of a dictionary with keys and values.

#In this we have created a dictionary by naming it as my_dict basically dictionary works on key and value pairs we can access its value by using [] and name of key in it  
#itself also we can access it by using get method in the real time projects genrally the line of code gets large in numbers at that time 
#instead of using any other method or searching the code we can directly use the keys to access that particular value genrally it saves time  

"""my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
}


print(my_dict["name"])  
print(my_dict.get("age"))  """

###############################################################################################################################################

#Write a Python script that takes input from the user and prints out a message based on the input type.

"""def input_type(user_input):
    # here we are checking that the input which user had provided can be converted into integer or not 
    try:
        int_value = int(user_input)
        print(f"You entered an integer: {int_value}")
    except ValueError:
        #if the input is not converted into integer then check that can it be converted into float
        try:
            float_value = float(user_input)
            print(f"You entered a float: {float_value}")
        except ValueError:
            #if it is also not a float then treat it as a string
            print(f"You entered a string: '{user_input}'")

#here we are taking inout from user
user_input = input("Please enter something: ")
#here we are calling our function
input_type(user_input)"""

####################################################################################################################################################

#Type conversion
"""my_string="hello"
my_list=list(my_string)
print(my_list)"""

#As in this we are doing type conversion from string to list by assiging the list to all the elements of string 

################################################################################################################################################

#How do you use regular expressions in Python for pattern matching?

#for pattern matching we can use 6 types of function used in re module
#1.re.match - it is only used to match the first string 
#2. re.seearch - it is genrally used to match any of the string if it is present
#3. re.findall - it returns a list of all non overlapping elements 
#4. re.finditer - it is used to find all non-overlapping matches of a regular expression pattern in a string
#5. re.sub - Replaces occurrences of the pattern with a specified string
#6. re.split - Splits the string at the occurrences of the pattern

"""import re
from re import search
pattern = r'programm'
text = 'python programm'

search = re.search(pattern, text)
if search:
    print("Match found:",search.group())
else:
    print("No match")"""
    
########################################################################################################################################

"""import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result  # Return the result of the original function
    return wrapper    
@timer_decorator
def example_function(n):
    #A simple function that simulates a time-consuming task
    total = 0
    for i in range(n):
        total += i
    return total

# Call the decorated function
result = example_function(1000000)
print(f"Result: {result}")"""