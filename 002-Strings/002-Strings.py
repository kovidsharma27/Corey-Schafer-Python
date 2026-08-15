# Prints Hello World
print('Hello World')

# type(variable) is used to know which type of variable it is. 
message='Hello World'
print(type(message))

message='Hello World'
print(message)

# This will cause an error because the apostrophe breaks the single-quoted string.
# For this python can not figure out where is starting and where's its ending.
# message='Bobby's World'
# print(message)

# We can use \ after a quote to tell python its not part of opening or closing.
message='Bobby\'s World'
print(message)

# """____""" or '''____''' can be used to write string in multiple lines.
message="""Bobby's World was a good
cartoon in 1990s."""
print(message)

# If we write "Hello Manav" then press enter by placing cursor in front of Manav, it will write it as following.
# Can also be done using ''. This can be used to write string in multiple lines.
# But the output will be in same line. 
message="Hello " \
"Manav"
print(message)

# len() is used here to give length of string, it also counts widespaces as part of string and its length.
message='Hello World'
print(len(message))

# To access individual character in a string.
message='Hello World'
print(message[0])
print(message[10])
# print(message[11]) will produce error : index out of range

# Slicing of a string, this code prints first 5 characters starting from 0 to 4.
message='Hello World'
print(message[0:5])

# .lower() and .upper() can be used to convert whole string to lower or upper case respectively.
# .title() is used to convert first character or character after a widespace to its upper case.
message='Hello World'
print(message.lower())
print(message.upper())
print(message.title())

# .count(value) is used to tell how many times the perticular value is appeared in a given string.
message='Hello World'
print(message.count('Hello'))
print(message.count('l'))
print(message.count('k'))

# .find() is used to find index of a character in a string.
# If we pass a group of characters it will return index of first character of that group from string.
message='Hello World'
print(message.find('World'))
print(message.find('H'))
print(message.find('l'))
print(message.find('k'))

# .replace(want to replace , new value) is used to replce a value of character from a string.
message='Hello World'
new_message=message.replace('World','Universe')
print(message)
print(new_message)
message=message.replace('World','Universe')
print(message)

# Concatenation of strings.
# + is used to concatenate strings.
greeting='Hello'
name='Michael'
message = greeting + name
print(message)
message = greeting +', '+ name
print(message)
message = greeting +', '+ name +'. Welcome!'
print(message)

# String formating. 
# {} is called place holder.
# .format(value) is used to format strings and to place value in place holders position.
greeting='Hello'
name='Michael'
message='{}, {}. Welcome'.format(greeting,name)
print(message)
# We can also use f-strings to directly put value in place holders position. 
message = f'{greeting}, {name}. Welcome!'
print(message)
# We can also use basic string methods inside formating.
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# Tells everthing that we can do with a variale, here name is a vaiable.
print(dir(name))

# Tells everthing that we can do with a string.
print(help(str))

# Tells everthing that we can do with a perticular method.
print(help(str.lower))
