# A list contains a list of values that can be homogenous and can also be nonhomogenous.
# Prints list.
cources=['History','Math','Physics','CompSci']
print(cources)

# Prints length of list.
print(len(cources))

# A list contains n values starting from 0 to n-1
# Prints individual elements of list.
print(cources[0])
print(cources[3])
print(cources[-1])

# Slicing of a list.
# In this example it will print values from 0 to 1 means it will print value at 0 and 1. 
print(cources[0:2])

# .append() is used to add value at end of a list.
cources=['History','Math','Physics','CompSci']
cources.append('Arts')
print(cources)

# .insert(index,value) is used to place value at a perticular position/index in a list.
cources=['History','Math','Physics','CompSci']
cources.insert(0,'Arts')
print(cources)

# .insert(index,list) can also add a list to another list at a perticular position.
cources=['History','Math','Physics','CompSci']
cources_2=['Arts','Education']
cources.insert(0,cources_2)
print(cources)

# Example showing how to access a list from a list, if a list is present in a list.
cources=['History','Math','Physics','CompSci']
cources_2=['Arts','Education']
cources.insert(0,cources_2)
print(cources[0])

# .extend(list) is used to add multiple values in a list by using another list
cources=['History','Math','Physics','CompSci']
cources_2=['Arts','Education']
cources.extend(cources_2)
print(cources)

# .append() in this example adds a list to another list in its ending positions.
cources=['History','Math','Physics','CompSci']
cources_2=['Arts','Education']
cources.append(cources_2)
print(cources)

# .remove(value) is used to remove a perticular value from a list.
cources=['History','Math','Physics','CompSci']
cources.remove('Math')
print(cources)

# .pop() removes last element from a list.
cources=['History','Math','Physics','CompSci']
cources.pop()
print(cources)

# We can use .pop() to remove last element and assign that to a variable.
# By doing this we can track what values we removed from our original list.
cources=['History','Math','Physics','CompSci']
popped=cources.pop()
print(popped)
print(cources)

# .reverse() is used to reverse a given list.
cources=['History','Math','Physics','CompSci']
cources.reverse()
print(cources)

# .sort() is used to sort a list in accending order.
# It sorts the original list.
# After using .sort() we will have no trace how that list looked before.
cources=['History','Math','Physics','CompSci']
cources.sort()
print(cources)

# .sort(), sort numbers from lowest to highest and string in alphabetical order.
cources=['History','Math','Physics','CompSci']
nums=[1,5,2,4,3]
cources.sort()
nums.sort()
print(cources)
print(nums)

# .sort(reverse=True) is used to sort in reverse order.
# Means in decanding order.
cources=['History','Math','Physics','CompSci']
nums=[1,5,2,4,3]
cources.sort(reverse=True)
nums.sort(reverse=True)
print(cources)
print(nums)

# sorted(list) dosen't modify a given list, instead it stores sorted one in new list.
cources=['History','Math','Physics','CompSci']
sorted_cources=sorted(cources)
print(sorted_cources)

# Basic fxns to find min,max,sum of a numerical list.
nums=[1,5,2,4,3]
print(min(nums))
print(max(nums))
print(sum(nums))

# list.index(value) is used to find a perticular index of a value in a list.
cources=['History','Math','Physics','CompSci']
print(cources.index('CompSci'))

# value in list is used to know if a value is present in a list or not.
# It returns boolian values like True or False.
cources=['History','Math','Physics','CompSci']
print('Math' in cources)
print('Art' in cources)

# Looping through a list and printing all its individual values.
cources=['History','Math','Physics','CompSci']
for cource in cources:
    print(cource)

# Looping through a list but instead of printing its values, here we are just printing the original list again.
cources=['History','Math','Physics','CompSci']
for cource in cources:
    print(cources)

# for index,value in enumerate(list) is used to get list values along with their indices/index.
cources=['History','Math','Physics','CompSci']
for index,cource in enumerate(cources):
    print(index,cource)

# for index,value in enumerate(list,start=1) is used to start index values from 1 instead of default 0.
cources=['History','Math','Physics','CompSci']
for index,cource in enumerate(cources,start=1):
    print(index,cource)

# variable = '_'.join(list) is used to join values of list seperated by _, and that variable will be of type string.
# in place of '_' we can use any string.
cources=['History','Math','Physics','CompSci']
cource_str=', '.join(cources)
print(cource_str)
print(type(cource_str))
cources=['History','Math','Physics','CompSci']
cource_str=' - '.join(cources)
print(cource_str)

# variable = string.split('_') can be used to split values of string by _, and that variable will be of type list.
# in place of '_' we can use any string inside split but it should be valid, means we should be able to seperate in that perticular way. 
cources=['History','Math','Physics','CompSci']
cource_str=', '.join(cources)
new_list=cource_str.split(', ')
print(cource_str)
print(new_list)
print(type(new_list))

# Here both the list are pointing at same iterable in memory, so changing one will change another. 
list_1=['History','Math','Physics','CompSci']
list_2=list_1
print(list_1)
print(list_2)
list_1[0]='Arts'
print(list_1)
print(list_2)

# Tuples are also used to store values in a form of list, but list are mutable where as tuples are non-mutable.
# Mutable be modification can be done like adding or removing elements, where for non-mutable it's not possible.
# Here both the tuples are pointing at same iterable in memory, so changing one will change another.
tuple_1=('History','Math','Physics','CompSci')
tuple_2=tuple_1
print(tuple_1)
print(tuple_2)

# This will cause error as tuples are immutaible.
# tuple1[0]='Arts'
# print(tuple_1)
# print(tuple_2)

# Sets -> They can store multiple values, but duplication is not allowed.
# Values stored at set don't have any fixed position, where as tuples and lists have fixed position elements.
# In simple way order is not important in sets, where as it is important in tuples and lists.
cs_cources={'History','Math','Physics','CompSci'}
print(cs_cources)

# If set found a duplicate value it will remove the other duplicates and keep only one unique value from that duplicates.
cs_cources={'History','Math','Physics','CompSci','Math'}
print(cs_cources)
# Here len(set) is used to show that set removed the duplicate value and length of set decreased.
print(len(cs_cources))

# value in set is used to check wheather a value is present in a set or not.
# This example will return boolean values such as True or False as per result.
cs_cources={'History','Math','Physics','CompSci'}
print('Math' in cs_cources)

# Just like union, intersection and difference in maths, we can also use them in python sets.
cs_cources={'History','Math','Physics','CompSci'}
art_cources={'History','Math','Art','Design'}

# set1.intersection(set2) will print the common elements in both the sets.
print(cs_cources.intersection(art_cources))
print(art_cources.intersection(cs_cources))

# set1.union(set2) will print all the elements present in both the sets.
print(cs_cources.union(art_cources))
print(art_cources.union(cs_cources))

# Will print values of cs_cources which are not present in art_cources.
print(cs_cources.difference(art_cources))
# Will print values of art_cources which are not present in cs_cources.
print(art_cources.difference(cs_cources))
