# variable = sorted(list) is a fxn that gives a new list which is sorted version of input list.
# Input list is not modified, instead new sorted list is returned.
li = [9,1,8,2,7,3,6,4,5] 
s_li = sorted(li) 
print('Sorted Variable:\t',s_li) # Output -> Sorted Variable:         [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Original Variable:\t',li) # Output -> Original Variable:       [9, 1, 8, 2, 7, 3, 6, 4, 5]

# list.sort() is a method that sorts the original list.
# modify the original list.
li = [9,1,8,2,7,3,6,4,5]
s_li = li.sort() # does not return a new list so s_li will be none
print('Sorted Variable:\t',s_li) # Output -> None
print('Original Variable:\t',li) # Output -> Original Variable:       [1, 2, 3, 4, 5, 6, 7, 8, 9]

# We can use variable = sorted(list,reverse = True) or list.sort(reverse = True) to sort a list in decending order.
li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li,reverse=True)
print('Sorted Variable:\t',s_li) # Output -> Sorted Variable:         [9, 8, 7, 6, 5, 4, 3, 2, 1]
li.sort(reverse=True)
print('Original Variable:\t',li) # Output -> Original Variable:       [9, 8, 7, 6, 5, 4, 3, 2, 1]

# tup = (9,1,8,2,7,3,6,4,5)
# tup.sort()
# Will give error because tuple has no attribute as .sort(), so we can not use .sort() method for tuple.

# sorted(tuple) can be used to sort a tuple.
# It returns a new list because sorted() always returns a list.
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t',s_tup) # Output -> Tuple    [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(s_tup)) # sorted() fxn always return a list, so after sorting a tuple the resulted variable will be a list.


di = {'name':'Corey','job':'programming','age':None,'os':'Mac'}
s_di = sorted(di) # Will sort keys of dictionary and return a list containing sorted keys.
print('Dict\t',s_di) # Output -> Dict     ['age', 'job', 'name', 'os']

li=[-6,-5,-4,1,2,3]
s_li=sorted(li)
print(s_li) # Output -> [-6, -5, -4, 1, 2, 3]

li=[-6,-5,-4,1,2,3]
s_li=sorted(li,key=abs) # key is called parameter, because of key = abs every value is passed through abs() fxn then compared for sorting.
# sort list in terms of absolute value of values in a list.
print(s_li) # Output -> [1, 2, 3, -4, -5, -6]

# class Employee():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
    
#     def __repr__(self):
#         return '({},{},${})'.format(self.name,self.age,self.salary)

# e1=Employee('Carl',37,70000)
# e2=Employee('Sarah',29,80000)
# e3=Employee('John',43,90000)

# employee=[e1,e2,e3]
# s_employee=sorted(employee)
# print(s_employee)
# will cause error as no key is given, so python don't know in what way it has to sort this.

'''
class	                     A blueprint for creating objects
__init__	                 Runs automatically to set up a new object's data
self	                     Refers to "this particular object"
__repr__	                 Controls how the object looks when printed
sorted(list, key=function)	 Sorts a list using a custom rule (the function tells it what to compare)
'''
class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employee=[e1,e2,e3]

def e_sort(emp):
    return emp.name
s_employee = sorted(employee,key = e_sort) # Will sort based on employee name
print(s_employee) # Output -> [(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employee=[e1,e2,e3]

def e_sort(emp):
    return emp.age
s_employee=sorted(employee,key = e_sort) # Will sort based on employee age
print(s_employee) # Output -> [(Sarah,29,$80000), (Carl,37,$70000), (John,43,$90000)]


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employee=[e1,e2,e3]

def e_sort(emp):
    return emp.salary
s_employee=sorted(employee,key =e_sort) # Will sort based on employee salary
print(s_employee) # Output -> [(Carl,37,$70000), (Sarah,29,$80000), (John,43,$90000)]


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employee=[e1,e2,e3]

def e_sort(emp):
    return emp.salary
s_employee=sorted(employee,key =e_sort,reverse=True) # Will sort based on employee salary in reverse order
print(s_employee) # Output -> [(John,43,$90000), (Sarah,29,$80000), (Carl,37,$70000)]


class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)
# created lambda fxn instead of def e_sort(emp) fxn
employee=[e1,e2,e3]
s_employee=sorted(employee,key = lambda e:e.name) # Will sort based on employee name
print(s_employee) # Output -> [(Carl,37,$70000), (John,43,$90000), (Sarah,29,$80000)]


from operator import attrgetter

class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('Carl',37,70000)
e2=Employee('Sarah',29,80000)
e3=Employee('John',43,90000)

employee=[e1,e2,e3]
s_employee=sorted(employee,key = attrgetter('age')) # will sort based on age
print(s_employee) # Output -> [(Sarah,29,$80000), (Carl,37,$70000), (John,43,$90000)] 
