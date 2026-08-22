# Comprehensions provide a concise way to create collections such as lists, dictionaries, and sets.
# Comprehension -> Easier, shorter, readable way of representation of code.

'''LIST COMPREHENSION'''

# 1.Code without comprehensions.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for n in nums:
    my_list.append(n)
print(my_list) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.Code with List comprehension for n
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [n for n in nums]
print(my_list) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.Using map and lambda fxn
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list of numbers 1-10
my_list = list(map(lambda n: n, nums))  # lambda takes n, returns n unchanged, map takes each value from nums and pass it through that fxn.
# list() converts result to a list
# equivalent simpler ways to do the same thing:
# my_list = nums.copy()
# my_list = list(nums) 
print(my_list)  # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2.Code without comprehensions.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2.Code with List comprehension for n*n
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [n * n for n in nums]
print(my_list) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2.Using map and lambda fxn
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = list(map(lambda n: n * n, nums))
print(my_list) # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
 

# 3.Code without comprehensions.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list) # prints [2, 4, 6, 8, 10]

# 3.Code with List comprehension for n if n is even
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [n for n in nums if n % 2 == 0]
print(my_list) # prints [2, 4, 6, 8, 10]

# 3.Using filter and lambda fxn
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list) # prints [2, 4, 6, 8, 10]

# Difference between map() and filter() ->
# 1. map() # map(function,iterable)                         
           # modify every item                          
           # dosen't follow any condition, can return any data-type/value             
           # return new transformed values
           # it produces one result for each input item
# 2. filter() # filter(function,iterable)
              # extract specific items
              # return only the values that follows given condition
              # returns the original values that pass the condition.
              # shorter or equal then input


# 4.Code without comprehensions.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []
for letter in "abcd":
    for num in nums[0:4]:
        my_list.append((letter, num))
print(my_list)

# 4.Code with List comprehension for (letter,num) pair using nums list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [(letter, num) for letter in "abcd" for num in nums[0:4]]
print(my_list)
# To do this using map we have to do from itertools import chain then use map and chain.
# This is very uneasy to do so we don't do this instead we just use comprehension or for loop.


# 5.Code without comprehensions.
my_list = []
for letter in "abcd":
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# 5. Code with List comprehension for (letter,num) pair using range() fxn
my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)


# zip(_,_) creates a list of tuples that contain same index values from different lists.
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolvarine", "Deadpool"]
print(list(zip(names, heros)))

# If the length of lists are different then zip() stops when the shortest iterable is exhausted.
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolvarine"]
print(list(zip(names, heros)))

'''DICTIONARY COMPREHENSION'''

# 1.Code without comprehensions.
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolvarine", "Deadpool"]
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

# 1.Code with Dictionary Comprehension of two list with all values
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolvarine", "Deadpool"]
my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)

# 2.Code without comprehensions.
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolvarine", "Deadpool"]
my_dict = {}
for name, hero in zip(names, heros):
    if name != "Peter":
        my_dict[name] = hero
print(my_dict)

# 2.Code with Dictionary Comprehension of two list with 'Peter' not included
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolvarine", "Deadpool"]
my_dict = {name: hero for name, hero in zip(names, heros) if name != "Peter"}
print(my_dict)

'''SET COMPREHENSION'''

# Code without comprehensions.
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# Code with set comprehensions.
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
my_set = {n for n in nums}
print(my_set) 
