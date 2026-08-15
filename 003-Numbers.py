# type() is used to see which type of variable it is.
num=3
print(type(num))
num=3.14
print(type(num))

# Few basic arithmetic operations.
print(3+2)
print(3-2)
print(3*2)
print(3/2)

# // perform division and rounds off to nearest integer.
print(3//2)
print(-7//2)

# n**m gives n to the power m. 
print(3**2)

# % gives remainder
print(3%2)

# This two examples shows precedence and associativity.
print(3*2+1)
print(3*(2+1))

# Shows both are used to increament by one
num=1
num=num+1
print(num)
num+=1
print(num)
# This type of things can also be done for *= -= /=
num=1
num*=10
print(num)

# Prints absolute value, value without sign.
print(abs(-3))

# round() is used to round off to nearest integer.
print(round(3.75))
print(round(3.21))
print(round(-3.75))
print(round(-3.21))
# rounds off to one decimal digit.
print(round(3.75,1))

# Shows relational operators and output in boolian that is True or False.
num_1=3
num_2=2
print(num_1==num_2)
print(num_1!=num_2)
print(num_1>num_2)
print(num_1<num_2)
print(num_1>=num_2)
print(num_1<=num_2)

# int() is used to convert string to integer type.
# Here using int() coverts num_1 and num_2 to integer and adds them.
num_1='100'
num_2='200'
print(int(num_1)+int(num_2))

# This example just covert string to integer and checks its type.
string='7'
integer_value=int(string)
print(type(integer_value))
