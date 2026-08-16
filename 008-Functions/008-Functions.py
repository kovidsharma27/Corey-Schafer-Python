# In function there are some specific instructions packed together to perform a specific task.
# We use def function_name(): to define a function.
# Fxn allow us to reuse code without writing it again and again.
# Using fxn makes our code clean and easy to edit.

# This is a function and inside a function some statements are written.
# But in this case we are writting pass inside fnx which means we are passing this fxn now and will come later to this.
# We can also use pass in if,elif,else statements also.
def hello_func():
    pass

# Below three examples - fxn1, fxn2 and fxn3 shows difference between fxn identity, fxn calling and printing return value of fxn respectively.  

# print(fxn_name) is used to know wheather a fxn exist or not, it shows fxn name and location in memory.
def hello_func1():
    pass
print(hello_func1) # Output -> <function hello_func1 at memory_location>

# fxn_name() is used to call a fxn, in simple words fxn calling means we are telling fxn to execute it's statements.
def hello_func2():
    print("Hello Function!")
hello_func2() # Output -> Hello Function!

# print(fxn_name()) is used to print return value of a fxn.
# In this example fxn is not executing anything, so return is None, so by doing this we can print None. 
def hello_func3():
    pass
print(hello_func3()) # Output -> None

# In this example we are calling a fxn and also printing it's return value.
def hello_func4():
    print("Hello Function!") # Output -> Hello Function! <- This came because of fxn calling.
print(hello_func4()) # Output -> None <- As return value of fxn is None.

# Suppose we have to replace ! -> . then we have to modify every statements where ! is written.
print("Hello!")
print("Hello!")
print("Hello!")
print("Hello!")
# Modified one.
print("Hello.")
print("Hello.")
print("Hello.")
print("Hello.")

# Instead of doing above repetative work we can just use a fxn, and whenever we have to modify something, we will just go to fxn and modify it's statement.
# In this example we are showing that we can modify a fxn statement and use that fxn multiple times where ever we want.
def hello_func5():
    print("Hello Function!")
hello_func5()
hello_func5()
hello_func5()
hello_func5()
# Modified one.
def hello_func6():
    print("Hello Function.")
hello_func6()
hello_func6()
hello_func6()
hello_func6()
# Here it can look un-necessary but for big programs it is very useful.

# return is used to retern/give result of group of statements or some statements.
# We can use return inside a fxn, if, elif, else and many more.

# In this example hello_func7 is returning a string, and we are calling hello_func7.
# But this fxn dosen't contain any print statement and we are calling fxn, not printing it's return value, so output will be blank.   
def hello_func7():
    return "Hello Function."
hello_func7() # Output -> 

# In this example we are printing return value of fxn so we can see output.
def hello_func8():
    return "Hello Function."
print(hello_func8())

# A pre-defined fxn takes a input and execute it's hidden code, generally written in C language and return an output.
# len() is a example of pre-defined fxn.
print(len("test"))
# len(input) Takes a input and count how many value are present in a data and return numeric counting result.

# This example fxn return a string, so we can use string operations here.
# hello_func9() -> Will give return value of fxn that is Hello Function.
# .upper() will convert all characters of Hello Function. to upper case and print will show output.
def hello_func9():
    return "Hello Function."
print(hello_func9().upper())

# fxn(parameter), A fxn can or can not take parameteres, A parameter is a place where input value will be passed in a fxn.
# We can pass arguments that will be passed to parameter as a input in a fxn and fxn will work on that input.
# fxn(number):
#    statement
# fxn(5)
# here 5 is argument and number is parameter, a fxn can take more then 1 parameter.

# We created a parameter but didn't pass a argument so it will give a error.
# def hello_func10(greeting):
#    return '{} Function.'.format(greeting)
# print(hello_func10())

# In this example "Hi" is an argument and greeting is a parameter.
# we are using .format() to place string in place holder and return it from fxn and print fxns return.
def hello_func10(greeting):
    return "{} Function.".format(greeting)
print(hello_func10("Hi"))

# In this example there a 2 parameters, greeting and name. and name is set to a default value that is a string.
# As one paramter is default we have a option to get only another paramter by passing an argument to a fxn, that's why we are passing only 1 argument here.
def hello_func11(greeting, name="You"):
    return "{} {}".format(greeting, name)
print(hello_func11("Hi"))

# In this example we have one parameter default but we can also change it's default value by passing a argument with same name as paramter with its new value.
# So name's default value that is You will be changed to Corey in this example. 
def hello_func12(greeting, name="You"):
    return "{} {}".format(greeting, name)
print(hello_func12("Hi", name="Corey"))

# We can also update parameters default value without using it's name in argument, we just have to be careful of positions in which we are passing the arguments.  
def hello_func13(greeting, name="You"):
    return "{} {}".format(greeting, name)
print(hello_func13("Hi", "Corey"))

# *args -> Takes positional arguments(value without key) and return a tuple containing those values.
# **kwargs -> Takes keyword value arguments and return a dictionary with those keys and their respective values.
# We use *args and **kwargs in a fxn parameter, where we don't know how many arguments we will pass.
# args and kwargs are just name, we can use any name in place of args and kwargs.

# In this example we pass few arguments in student_info fxn and positional arguments goes to *args and keyword value arguments goes to **kwargs.
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
student_info("Math", "Art", name="John", age=22)

# If we pass a variable of dictionary, list, tuples it will be passed to *args
def student_info1(*args, **kwargs):
    print(args)
    print(kwargs)
cources = ["Math", "Art"]
info = {"nmae": "John", "age": 22}
student_info1(cources, info)
# We can also pass tuples.
def student_info1(*args, **kwargs):
    print(args)
    print(kwargs)
cources = ("Math", "Art") 
info = {"nmae": "John", "age": 22}
student_info1(cources, info)

# So to improve above unexpected output we have to specify what we are passing in parameter.
# *cources in fxn argument will pass each value of cources to *args parameter.
# **info in fxn argument will pass each value of info to **kwargs parameter.
def student_info2(*args, **kwargs):
    print(args)
    print(kwargs)
cources = ["Math", "Art"]
info = {"nmae": "John", "age": 22}
student_info2(*cources, **info)

# key = value is used in fxn arguments to specify that this is key and that is it's value.
# Where as key:value is used to create key value pair in dictionary.

# Number of days per month. First value is a placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Below example is to check wheather a year is leep year or not.
def is_leap(year):
    """Return True for leap year, False for non-leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# In this fxn we return number of days of a month and for febuary we take help of is_leap(year) fxn.
def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]
print(is_leap(2017))
print(is_leap(2020))
print(days_in_month(2017, 2))
print(days_in_month(2020, 11))
