# We've all run into errors and exceptions while writing Python programs. 
# Here we will learn how we can handle exceptions in specific ways and also look at the control flow of a try/except/else/finally statement. 
# Understanding how to properly handle errors will provide us with the tools to make better software in the future.

'''
Sample test_file.txt used ->

Test File Contents!
'''

# f = open('testfile.txt')
# Output -> After executing we get =>
# f = open('testfile.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'testfile.txt'

# As a developer this errors help us to find the error and gives information what that error is.
# But we don't want to display this to the people who are using our software.
# So this is one of the reason to use Try/Except Blocks.

# If we can anticipate sections of our code that might throw an error or an exception then we can use this Try/Except Blocks to handle them in the way we wanted.

# If we do this then we can get our custom errors instead of the error that python shows in terms for a developer.
try:
    f = open('testfile.txt') 
except Exception: # An exception in Python is an error that occurs during the execution of a program (at runtime)
    print('Sorry. This file does not exist')
# Output -> Sorry. This file does not exist
# With-in try block we are going to run some code and if this throws an exception,
# Then we go to our except block and execute code that we wanted to run if an exception occurs in try block.

# Exception catches a lot of errors not just FileNotFoundError.
try:
    f = open('test_file.txt') 
    var = bad_var
except Exception: 
    print('Sorry. This file does not exist')
# Output -> Sorry. This file does not exist

# So, because of this we should be more specific about error.
# try:
#     f = open('test_file.txt') 
#     var = bad_var
# except FileNotFoundError: 
    # print('Sorry. This file does not exist')
# Output -> Will get regular python error.
#     var = bad_var
#           ^^^^^^^
# NameError: name 'bad_var' is not defined

try:
    f = open('test_file.txt') 
    var = bad_var
except FileNotFoundError: 
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')
# Output ->
# Sorry. Something went wrong 

# We can also print python error warning in short instead of custom messages.
try:
    f = open('test_file.txt') 
    var = bad_var
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print(e)
# Output ->
# name 'bad_var' is not defined

try:
    f = open('test_file.txt') 
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print(e)
# Output ->
# No error came so no output.

try:
    f = open('testfile.txt') 
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print(e)
# Output -> [Errno 2] No such file or directory: 'testfile.txt'

# If no error in try block then else block will execute.
try:
    f = open('test_file.txt') 
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
# Output -> 
# Test File Contents!

# finally block runs no matters if error is there or not.
try:
    f = open('test_file.txt') 
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
# Output -> 
# Test File Contents!
# Executing Finally...

try:
    f = open('testfile.txt') 
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
# Output ->
# [Errno 2] No such file or directory: 'testfile.txt'
# Executing Finally...

# We can also raise/make our own exceptions 
try:
    f = open('test_file.txt')
    if f.name == 'test_file.txt':
        raise Exception
except FileNotFoundError as e: 
    print(e)
except Exception as e:
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
# Output ->
# Error
# Executing Finally...


'''
Some Knowledge about Exceptions and Error Handling ->

try: Runs the risky code that might cause an error.
except: Catches and handles the error if one occurs inside the try block.
else: (Optional) Runs code only if no exceptions were raised in the try block.
finally: (Optional) Runs no matter what, whether an error happened or not. This is great for clean-up tasks like closing files or database connections.

Some common Built-in Exceptions ->

ZeroDivisionError: Dividing any number by zero is impossible and breaks the math rules.

OverflowError: A numeric calculation produces a result that is too large for Python to handle.

FloatingPointError: An internal problem occurred during a decimal (floating-point) math operation.

IndexError: You tried to access a list item using an index that does not exist.

KeyError: You looked for a dictionary key that is missing or spelled wrong.

AttributeError: You called a method or variable that the object does not have.

NameError: You used a variable or function name that has not been defined.

UnboundLocalError: You referenced a local variable before assigning it a value inside a function.

TypeError: You tried to combine or operate on incompatible data types, like text and numbers.

ValueError: A function got the right data type but an inappropriate value, like turning "abc" into an integer.

FileNotFoundError: Python could not find the file at the path you provided.

PermissionError: You do not have the system permissions required to access a file or folder.

ModuleNotFoundError: You tried to import a library or module that is not installed.

ImportError: Python found the module, but could not find the specific function or class inside it.

SyntaxError: Your code contains a typo or grammar mistake that violates Python's language rules.

IndentationError: Your code has incorrect spacing or mixed tabs at the start of a line.

KeyboardInterrupt: The program was manually stopped by the user, usually via Ctrl+C.

StopIteration: A loop mechanism was told to get the next item, but the iterator is empty.

MemoryError: Your script ran out of available system memory (RAM) to complete an operation.

RuntimeError: A generic error occurred that does not fit into any other specific category.
'''


'''
In Python, all exceptions are organized in a tree-like class hierarchy. 
At the very top sits BaseException, and almost all built-in errors inherit from a branch called Exception.

When you catch a parent exception in a try...except block, it will automatically catch all of its child exceptions as well.

Hierarchy of exception names ->

BaseException (The absolute root)

    KeyboardInterrupt (Triggered by Ctrl+C)
    SystemExit (Triggered when sys.exit() is called)
    Exception (The parent of all regular application errors)

        ArithmeticError
            ZeroDivisionError
            OverflowError
            FloatingPointError

        LookupError
            IndexError
            KeyError

        OSError (System/Environment errors)
            FileNotFoundError
            PermissionError

        SyntaxError
            IndentationError

        AttributeError

        NameError
            UnboundLocalError

        TypeError

        ValueError

        ImportError
            ModuleNotFoundError

        RuntimeError

        StopIteration

Hierarchy Matters: The Ordering Rule
Because catching a parent class catches all its children, you must always list your except blocks from most specific (child) to most general (parent).

Example ->

Incorrect Ordering (Broken logic) :
try:
    result = 10 / 0
except Exception: # This matches everything under Exception, including ZeroDivisionError
    print("Caught a general exception!") 
except ZeroDivisionError: # Python will never reach this block
    print("Caught a division by zero!")

Correct Ordering (Specific to General) :
try:
    result = 10 / 0
except ZeroDivisionError: # Checked first
    print("Caught a division by zero!")
except Exception: # Acts as a backup fallback for any other error
    print("Caught some other error!")
'''
