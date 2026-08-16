# A loop is used to perform multiple repetative steps for a operation or a task.
# There are two basic type of loops in python that is for loop and while loop.
# for loop executes for perticular steps where as while loop execute until condition is True.

# This example loops through a list called nums and print values at a step.
# loops take a value from nums and put it in num and print(num), and perform same for other values in nums.
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# break statement is used to stop loop at a perticular step.
# It is mostly used to increase efficiency.
# In this step we stop looping when we reach 3 and print("Found!") 
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

# In this example when we reach 3 we print it then print "Found!" and stop our loop.
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
    if num == 3:
        print("Found!")
        break

# continue statement is used to skip a value from operation while looping.
# In this example when we reach 3 we print("Found!") and skips printing 3 and move to next value.
# By placing continue at a condition and if condition True then it will skip operations below continue in a loop and move to next value. 
nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)

# This is an example of nested loop.
# In nested loop, for each value of outer loop inner loop will execute for n times.
# In this example we take a value from nums and and for that value we print each character from "abc" one time.
nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in "abc":
        print(num, letter)

# range(integer_n) is used to perform looping n number of times.

# In this example we loop 10 times from 0-9 and print each value.
for i in range(10):
    print(i)

# range(starting, ending) by doing this we can specify starting point/value of range.
# range(starting, ending), range will always skip the ending means range will also execute < ending.
for i in range(1, 11):
    print(i)

# range(starting, ending, step) by doing this we can increase/decrease steps.
# Means by placing step range will increament/decreament it's value by that perticular step.
# This can be used to skip, increament, decreament, reverse values from range fxn. 
for i in range(2, 11, 2):
    print(i)
for i in range(10, 1, -2):
    print(i)

# While loop execute until condition is True
# So in this example we increament x by 1 in each step, and loop will execute while x is smaller then 10.
# So loop will run for 10 steps from 0-9 and print value of each step.
x = 0
while x < 10:
    print(x)
    x += 1

# This example showcase that we can also use break statements in while loop.
# And we can also use continue statement in while loop. 
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# In this example condition is always True, so to stop this loop we will use break statement.
# For this example when we reach 5, looping will stop.
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

# This is an example of infinite loop.
# Here condition is always True and here no break statement is used, it will execute infinitely.
# x = 0
# while True:
#     print(x)
#     x += 1
# If by mistake you execute infinite loop, then to stop it press ctrl + c
