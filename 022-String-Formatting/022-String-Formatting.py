# Now we use string concatenation means using + to combine different strings.
# But it has many flaws like ->
# 1. It is not very readeable 
# 2. We have to use + many times in different locations
# 3. Wide-spaces are very important for desiered output using concatenation
# 4. Have to convert integer and other similar objects to string as concatenation supports string type value only, so str(object) will be used.  

person={'name':'Jenn','age':23}
sentence='My name is '+ person['name']+' and I am '+ str(person['age'])+ ' years old.'
print(sentence) # Output -> My name is Jenn and I am 23 years old.
# It gives desiered output but there are better ways to do this.

# We can use string formating .format(value) to improve draw-backs of string concatenation.
# .format() is used after closing of string.
# {} are called place holders, it is the place in string where value will be displayed or replacement field. 
person={'name':'Jenn','age':23}
sentence='My name is {} and I am {} years old.'.format(person['name'],person['age'])
print(sentence) # Output -> My name is Jenn and I am 23 years old.

# If we don't specify position in place-holder then first pass will be given to first place-holder from left and second pass will be given to second place holder from left. 
# In .format(), positional indexes start at 0.

# With out using dictionary.
sentence='My name is {} and I am {} years old.'.format('Manav','19')
print(sentence) # Output -> My name is Manav and I am 19 years old.

person={'name':'Jenn','age':23}
sentence='My name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentence) # Output -> My name is Jenn and I am 23 years old. 
# first value in .format() will be passed to place-holder with 0 position and second value will be passed to place-holder with 1 position.

# We can also use place-holders for values that need or is repeated.
tag = 'hi'
text = 'This is a Headline'
sentence = '<{0}>{1}</{0}>'.format(tag,text) 
print(sentence) # Output <hi>This is a Headline</hi> 

person={'name':'Jenn','age':23}
sentence='My name is {0[name]} and I am {1[age]} years old.'.format(person,person)
print(sentence) # Output -> My name is Jenn and I am 23 years old.  

# Improved version of above code.
person={'name':'Jenn','age':23}
sentence='My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence) # Output -> My name is Jenn and I am 23 years old.

# Can also use .format(list) is used for string formating 
l = ["Jenn",23]
sentence='My name is {0[0]} and I am {0[1]} years old.'.format(l)
print(sentence) # Output -> My name is Jenn and I am 23 years old. 

# We can also access attributes in a similar way.
class person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age
p1 = person("Jack",33)
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence) # Output -> My name is Jack and I am 33 years old. 

# We can also pass keyword arguments in .format(key=value)
sentence = "My name is {name} and I am {age} years old.".format(name = "Jenn", age = 23)
print(sentence) # Output -> My name is Jenn and I am 23 years old. 

# We can also use **dictionary to unpack any dictionary
# **dictionary unpacks the dictionary so its keys can be used as keyword arguments.
person={'name':'Jenn','age':23}
sentence = "My name is {name} and I am {age} years old.".format(**person)
print(sentence) # Output -> My name is Jenn and I am 23 years old.

# Formatting with numbers ->

for i in range(1,11):
    sentence = "The value is {}".format(i)
    print(sentence) 
# Prints "The value is 1", "The value is 2", ... up to "The value is 10".

# {:02} means a minimum width of 2 with leading zeros,
for i in range(1,11):
    sentence = "The value is {:02}".format(i)
    print(sentence) 
# Prints "The value is 01", "The value is 02", ... up to "The value is 10".

# {:03} means a minimum width of 3 with leading zeros.
for i in range(1,11):
    sentence = "The value is {:03}".format(i)
    print(sentence) 
# Prints "The value is 001", "The value is 002", ... up to "The value is 010".

# :.2f means 2 digits after the decimal point.
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence) # Output -> Pi is equal to 3.14

pi = 3.14159265
sentence = 'Pi is equal to {:.3f}'.format(pi)
print(sentence) # Output -> Pi is equal to 3.142

# :, adds thousands separators.
sentence = "1 MB is equal to {:,} bytes".format(1000**2)
print(sentence) # Output -> 1 MB is equal to 1,000,000 bytes

sentence = "1 MB is equal to {:,.2f} bytes".format(1000**2)
print(sentence) # Output -> 1 MB is equal to 1,000,000.00 bytes

import datetime
my_date = datetime.datetime(2016,9,24,12,30,45)
print(my_date)

import datetime
my_date = datetime.datetime(2016,9,24,12,30,45) #(year,month,day,hour,minute,second)
sentence = '{:%B %d, %Y}'.format(my_date) # Telling python that we want my_date in this format.
# %B -> Month_name | %d -> day | %Y -> Year | Got this from python documentation.
print(sentence) # Output -> September 24, 2016

import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence) # Output -> September 24, 2016 fell on a Saturday and was the 268 day of the year 
# %A is for week day name and %j is to get date number from 365/366 days of year/leap-year. 
