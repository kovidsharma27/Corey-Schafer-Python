# Scope variable follows LEGB rule which determines from where variables can be accessed.

# L -> Local -> Variables defined within a fxn.
# E -> Enclosing -> Variables in the local scope of enclosing fxns.
# G -> Global -> Variables defined at the top of the module or explicitly declared global.
# B -> Build-in -> Names that are pre-assigned in python.

# Python checks a variable first in Local scope then Enclosing scope then Global scope and then Built-in fxns.

x = "global x" # It is global because it's in main body of our module.
def test1():  
    y = "local y" # y is local to this test1 fxn, means it can be accessed from test1 fxn only.
    print(y)
test1()


x = "global x"
def test2():
    y = "local y"
    print(x)
test2()
# 1.Is x in local scope of this test2 fxn -> No
# 2.Is x in enclosing fxn of this test2 fxn -> No
# 3.Is x a global variable -> Yes
# So now python print's x.


x = "global x"
def test3():
    y = "local y"
    print(x)
test3() # Call test3 fxn and inside test3 fxn there is a print statement for x, so it prints x.
'''print(y)''' # This will cause an error.
# As y is a local variable of test3 fxn only, so python know that y exist inside that test3 fxn only.
# So if we try to access y outside of it's container fxn without calling it's container fxn then it will cause an error.


x = "global x"
def test4():
    y = "local y"
    print(x)
test4()
print(x)
# x is a global variable so it can be accessed inside or outside the fxn.


x = "global x"
def test5():
    x = "local x" # This x is local to this test5 fxn only. Because it's defined inside test5 fxn.
    print(x) # Follows LEGB rule so first checks is x in local scope -> yes, so prints x which is in local scope
    print(id(x)) # example -> 1566742155392
test5()
print(x) # Prints global x as python don't know that there is another x inside test5 fxn.
print(id(x)) # example -> 1566742185456
# Both the id's are different means both x are different in memory.


x = "global x"
def test6():
    global x
    x = "local x"
    print(x)
test6()
print(x)

'''we can use -> global variable_name <- inside a fxn to make any variable as global variable.''' 
def test7():
    global x
    x = "local x"
    print(x) # Output -> local x
test7()
print(x) # Output -> local x


def test8():
    x = "local x"
    print(x) # Output -> local x
test8()
# print(x) -> NameError: name 'x' is not defined
# As x is local to test8 fxn only, can not be accessed outside of that fxn.


def test9(z): # z is also a local variable called parameter which can take input values.
    print(z) # Output -> local z
test9("local z") # fxn_name(argument) is used to pass values to parameter of a fxn.


def test10(z):
    print(z)
test10("local z") # Output -> local z
# print(z) NameError: name 'z' is not defined
# As z is local to test10 fxn only.


# min() fxn is an example of built-in functions. 
m = min([5, 1, 4, 2, 3]) # Find's the minimum value from iterable of values and store that minimum value to m variable.
print(m) # Output -> 1

# To view builtins we can do this. 
import builtins
print(dir(builtins))
# Built-in contains exceptions, error_name and built-in functions. 


# def min():
#     pass
# pass means do nothing to this fxn now.

# python allow us to use built-in function names to create our own function.
# But it's generally not a standard way to write a fxn name.
# def min(): We created a fxn named min() which takes 0 arguments.
#     pass
'''m = min([5, 1, 4, 2, 3])''' # This will cause a TypeError: min() takes 0 positional arguments but 1 was given.
print(m)
# This min() built-in fxn which gives minimum value of a iterable, didn't worked. 
# This happened bacause python fist checks min in local scope -> No, then Enclosing -> No, then global -> yes "def min()".
# Because of this it didn't checked built-in scope.


def my_min():
    pass
m = min([5, 1, 4, 2, 3])
print(m)
# This will work as usual.


# Now we will see concept of Enclosing scope which is very important.
# This concept is applied for nested functions means functions inside a function.
'''  def fxn_1():
        v -> variable
        def fxn_2():
            statement  '''
# fxn_1() is enclosing fxn of fxn_2() and v is in local scope of enclosing fxn.
    
    
def outer():
    x = "outer x" # x is local to outer() and is in the enclosing scope of inner().
    def inner():
        x = "inner x" # This x is local for inner fxn only.
        print(x) # LEGB rule -> local scope of inner fxn -> yes.
    inner() # Output -> inner x
    print(x) # LEBG rule -> local scope for outer fxn -> yes.
outer() # Output -> outer x


def outer():
    x = "outer x"
    def inner():
        print(x) # LEGB rule -> local scope -> No then local scope of enclosing fxn -> yes.
    inner() # Output -> outer x
    print(x)
outer() # Output -> outer x


def outer():
    x = "outer x"
    def inner():
        nonlocal x  # This tells Python: x here is NOT a new local variable —
                    # it refers to the x that already exists in outer().
        x = "inner x"  # So this line modifies outer()'s x directly,
                       # not a separate copy inside inner().
        print(x)  # Prints outer()'s x, now changed to "inner x"
    inner()
    print(x)  # Also prints "inner x", since outer()'s x was actually modified
outer()
# nonlocal makes inner() fxn skip creating its own local variable and borrow/share the outer one instead.


x = "global x"
def outer():
    x = "outer x"
    def inner():
        x = "inner x"
        print(x)
    inner() # Output -> inner x
    print(x) 
outer() # Output -> outer x
print(x) # Output -> global x


x = "global x"
def outer():
    x = "outer x"
    def inner():
        print(x) 
    inner() # Output -> outer x
    print(x)
outer() # Output -> outer x
print(x) # Output -> global x


x = "global x"
def outer():
    def inner():
        print(x)
    inner() # Output -> global x
    print(x)
outer() # Output -> global x
print(x) # Output -> global x  
