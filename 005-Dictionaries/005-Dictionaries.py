# Dictionaries is used to store key:value pair where each each is assigned a value.
# The key can be used to access its assigned value.
# Key can be anything and same for value also.

# This example prints a dictionary
student={'name':'John','age':25,'cources':['Math','CompSci']}
print(student)

# Accessing value by using its key -> dictionary[key] this will give value of that key.
print(student['name'])
print(student['cources'])
student={1:'John','age':25,'cources':['Math','CompSci']}
print(student[1])

# This will cause error because that perticular key dosen't exist in our dictionary.
# student={'name':'John','age':25,'cources':['Math','CompSci']}
# print(student['phone'])

# We can also use dictionary.get(key) to access its perticular value.
student={'name':'John','age':25,'cources':['Math','CompSci']}
print(student.get('name'))

# If a key dosen't exist in our dictionary and we use dictionary.get(key) it will return None. 
student={'name':'John','age':25,'cources':['Math','CompSci']}
print(student.get('phone'))

# We can also show a output if the perticular key dosen't exist in our dictionary by using dictionary.get(key,output).
student={'name':'John','age':25,'cources':['Math','CompSci']}
print(student.get('phone','Not Found'))

# If dictionary_1 already exist and we do dictionary_1[key]=value, it will add that key:value pair at end of dictionary_1.
student['phone']='555-5555'
print(student)
print(student.get('phone'))

# If a key exist in our dictionary and we use .get(present_key,default_value) 
# Then it will ignore default_value and will print original value that is already present in dictionary.
# In this example Not Found will be ignored and 555-5555 will get printed.
student={'name':'John','age':25,'cources':['Math','CompSci']}
student['phone']='555-5555'
print(student.get('phone','Not Found'))

# We can also update a key for it's new value by using dictionary[key] = New value. 
student={'name':'John','age':25,'cources':['Math','CompSci']}
student['phone']='555-5555'
student['name']='Jane'
print(student)

# We can use dictionary.update({key1:value1, key2:value2, key2:value3}) to update multiple values at once.
# If a key is already present then it will be updated.
# If a key is not present then it will be added to the dictionary.
student={'name':'John','age':25,'cources':['Math','CompSci']}
student.update({'name':'Jane','age':26,'phone':'555-5555'})
print(student)

# We can use del dictionary[key] to delete a key:value pair from our present dictionary.
student={'name':'John','age':25,'cources':['Math','CompSci']}
del student['age']
print(student)

# We can also use dictionary.pop(key) to remove a perticular value form present dictionary.
student={'name':'John','age':25,'cources':['Math','CompSci']}
student.pop('age')
print(student)
# We can also use variable = dictionary.pop(key) to store a removed key.
# We can not do this by using del dictionary[key].
student={'name':'John','age':25,'cources':['Math','CompSci']}
age=student.pop('age')
print(age)

# len(dictionary) prints length of dictionary.
# for dictionary length = number of keys present in dictionary.
student={'name':'John','age':25,'cources':['Math','CompSci']}
print(len(student))


student={'name':'John','age':25,'cources':['Math','CompSci']}
print(student.keys())
# Output -> dict_keys(['name', 'age', 'cources']) Show all the key present in dictionary.
print(student.values())
# Output -> dict_values(['John', 25, ['Math', 'CompSci']]) Show all the values present in dictionary.
print(student.items())
# Output -> dict_items([('name', 'John'), ('age', 25), ('cources', ['Math', 'CompSci'])]) Shows all the items present in a dictionary.

# By simply looping through a dictionary we get all the key present in dictionary.
student={'name':'John','age':25,'cources':['Math','CompSci']}
for key in student:
    print(key)

# By doing this we get all the keys along with their values.
student={'name':'John','age':25,'cources':['Math','CompSci']}
for key, value in student.items():
    print(key, value)
