# A module that contain a print statement, a test string and a fxn.
# This module name is my_module.
print("Imported my_module...")
test = "Test String"

# A simple linear search that return index of a value if it's equal to target, Time complexicity -> O(n), Space complexicity -> O(1). 
def find_index(to_search, target):
    """Find the index of a value in a sequence."""
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
# Above code was created in my_module.
# If we run above my_module it will print -> Imported my_module...

# Suppose we want to use my_module's code in another module then we can import my_module to that module.
# Means we can import a module's fxn and programs to another module or file and use them instead of coding everthing from scratch.


# Below code was created in .py file named test.

# There are different ways to import a module and it's fxns in another module or file.
# If imported module and current file are in same folder then we can simply import it by doing this operations.
# Imported module and their fxns are always written on top of script, so that they can be used everwhere in our script.
# But here for explenation i have imported them in between.

# I am writing import my_module's code in '''___''' as this is a form of comment, and this code will not give error.
# To run this correctly, create a my_module.py file and write above code in it and create a test.py file in same folder/directory and write below code in it.

'''
# Passing cources list in to_search parameter in find_index fxn and passing "Math" as target in target parameter.
# Storing return value of find_index fxn in index and printing it.
import my_module
cources = ["History", "Math", "Physics", "CompSci"]
index = my_module.find_index(cources, "Math")
print(index)

# Using mm in place of my_module name.
import my_module as mm
cources = ["History", "Math", "Physics", "CompSci"]
index = mm.find_index(cources, "Math")
print(index)

# We can also do this because we directly imported find_index from my_module.
from my_module import find_index
cources = ["History", "Math", "Physics", "CompSci"]
index = find_index(cources, "Math")
print(index)

# Importing find_index fxn and test string from my_module.
from my_module import find_index, test
cources = ["History", "Math", "Physics", "CompSci"]
index = find_index(cources, "Math")
print(index)
print(test)

# Importing my_module's find_index fxn as fi and test string.
from my_module import find_index as fi, test
cources = ["History", "Math", "Physics", "CompSci"]
index = fi(cources, "Math")
print(index)
print(test)

# This line will show warning because this imports everthing from my_module and makes a confusion that what is from my_module and what is from test file.
# But everthing will execute.
from my_module import * 
cources = ["History", "Math", "Physics", "CompSci"]
index = find_index(cources, "Math")
print(index)
print(test)   
'''

# Python checks multiple locations when we import something, and this locations can contain our imported module.
# Locations are added in a list called sys.path
# To see that locations we have to import system module by writing import sys and print(sys.path)
import sys
print(sys.path) # A lot of locations in a list will appear.

# We can manually add new locations using sys.path.append('new_location')
import sys
sys.path.append('new_location') # This will add new_location in end of our sys.path list as we are using .append()
print(sys.path)

# We can manually remove old locations using sys.path.remove('old_location')
import sys
sys.path.remove('new_location') # I am removing a location named new_location as it's already in our sys.path
print(sys.path)
# sys.path is a temperory add or remove statement means when we close our file, all the modified directory will be set back to default.

# To permanently add a new directory we have to follow some steps.
# For Windows.
# 1. Right click on my Pc -> Show more Options -> Properties
# 2. Advanced system settings -> Environment Variables
# 3. new -> Fill variable name as PYTHONPATH and location (Open a file -> Right click -> Properties -> Then copy location from there)
# 4. Click OK few times in each window and close everything.
# 5. Open cmd -> Type py or python -> import sys -> print(sys.path)
# To delete reverse the steps.

# Some standard libaries ->>

import random 
cources = ['History','Math','Physics','CompSci']
# random.choice(list) is used to chose a random value from a list.
random_cources = random.choice(cources) # Takes a random value from cources list and store that value in random_cources variable.
print(random_cources) # This will print value stored in random_cources.

import math # Contain some mathematical fxns and methods.
rads = math.radians(90) # Takes a input as degree and convert it into radian and store it to rads.
print(rads) # prints rads
print(math.sin(rads)) # Takes a radian or degree input in sin fxn and return sin of that and prints it.

import datetime
import calendar
today = datetime.date.today() # Store todays date in yyyy-mm-dd format.
print(today) # prints todays date.
print(calendar.isleap(2020)) # prints a boolean value True if leap_year or False if not leap_year as per input year. 

import os 
print(os.getcwd()) # prints current directory where script is located.

import os 
print(os.__file__) # Shows location where os module is located.
# We can do this with other modules also but not with every module.

# code C:\Users\user_name\AppData\Local\Programs\Python\Python_version\Lib
# user_name can be your pc user name and Python_version can be Python314 that is python 3.14
# Type this in terminal of vs code, new vs code window will open with all standard libaries with their source code.
