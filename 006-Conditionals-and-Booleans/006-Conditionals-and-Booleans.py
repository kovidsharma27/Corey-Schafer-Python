# If condition is True then if block statements will execute, if False then it will not execute.
if True:
    print('Conditional was True')
if False:
    print('Conditional was True')

# Here relational operator is used in if's condition.
# For this example condition is True so if block statements will execute.
language='Python'
if language == 'Python':
    print('Conditional was True')

# Here we have if / else.
# When if condition is True then it's block statments will execute.
# When if condition is False then else block statements will execute.
# Here in this example if condition is True so if block statements will execute.
language='Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# Here in this example if condition is False so else block statements will execute.
language='Java'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# Here we have if, elif, else.
# First it will check if condition, when True if block statements will execute, when False it will check elif condition.
# In second step elif condition will be checked, when True elif block statements will execute, when False it will execute else block statements.
# So for this example elif will be executed.
language='Java'
if language == 'Python':
    print('Language is Python')
elif language=='Java':
    print('Language is Java')
else:
    print('No match')

# When multiple elif are there and if condition is False, then it will check all elifs conditions.
# Here first elif block will be executed.
language='Java'
if language == 'Python':
    print('Language is Python')
elif language=='Java':
    print('Language is Java')
elif language=='JavaScript':
    print('Language is JavaScript')
else:
    print('No match')

# Here boolian value is stored in a variable.
# Here and operator is used so both the condition in if condition should be True.
# In this example if block statements will be executed.
user = 'Admin'
logged_in=True
if user=='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Here and operator is used and one condition from if conditions is False so else block statements will be executed.
user = 'Admin'
logged_in=False
if user=='Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Here or operator is used so any one condition from if conditions should be True.
# So as per this example if block statements will be executed.
user = 'Admin'
logged_in=False
if user=='Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Here not operator is used, so not True = False and not False = Ture.
# So for this example if block statements will be executed.
user = 'Admin'
logged_in=False
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

# == checks if value is equal.
# is checks if they are pointing at same thing in memory.
# This examples returns boolian results such as Ture or False.

a=[1,2,3]
b=[1,2,3]
print(a==b) # True
print(a is b) # False

a=[1,2,3]
b=a
print(a==b) # True
print(a is b) # True

# id(variable) is used to see where object is stored in memory.
# id() shows a id related to a position in memory.

# In this example ids of both will be different.
a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))

# In this example ids of both will be same.
a=[1,2,3]
b=a
print(id(a))
print(id(b))

a=[1,2,3]
b=a
print(a is b) # True
print(b is a) # True
print(id(a)==id(b)) # True

# when [], (), {}, '', 0, None, False are present in condition, then condition will be False in this cases.
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ''
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ()
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

# Any other value then above listed is equal to True.
condition = 10
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 'Luck'
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
