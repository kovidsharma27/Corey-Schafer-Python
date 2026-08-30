# Problem -> 
# The downloaded video files are not sorted correctly because their filenames start with titles instead of the video number. 
# With hundreds of videos, manually renaming them would take too much time.

# What we will do -> 
# We’ll create a Python script to automatically rename the files, moving the video number to the beginning of each filename. 
# This will make the videos sort and play in the correct order automatically.

'''
Files that we have to arrange ->

Earth - Our Solar System - #4.mp4
Jupiter - Our Solar System - #6.mp4
Mars - Our Solar System - #5.mp4
Mercury - Our Solar System - #2.mp4
Neptune - Our Solar System - #8.mp4
Pluto - Our Solar System - #10.mp4
Saturn - Our Solar System - #7.mp4
The Sun - Our Solar System - #1.mp4
Uranus - Our Solar System - #9.mp4
Venus - Our Solar System - #3.mp4
'''

import os

os.chdir("Path_where_this_files_are") # change directory to path that we passed
print(os.getcwd()) # prints current working directory

# os.listdir() will give a list containing files names of current working directory.
# We are looping through that list and printing one file name at a time.
for f in os.listdir():
    print(f)
# This will print all above mentioned files each in new line.
# Output -> Earth - Our Solar System - #4.mp4 ........ Venus - Our Solar System - #3.mp4

# when writing a script, it is better to build the solution step by step rather than trying everything at once.
# First, change the directory and check the current directory to make sure you are in the right place. 
# Then, loop through all the files and print the files to confirm they are being detected correctly. 
# Finally, build the solution gradually, testing each step before moving to the next.

for f in os.listdir():
    print(os.path.splitext(f)) # Will print a tuple with first value as name of file and second as extension of file
# Will perform this for all files names in current directory.
# Output -> ('Earth - Our Solar System - #4', '.mp4') ........ ('Venus - Our Solar System - #3', '.mp4')

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) # First value of tuple will be in f_name second will be in f_ext
    print(f_name) # prints f_name 
# Output -> Earth - Our Solar System - #4 ......... Venus - Our Solar System - #3

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    print(f_name.split('-')) # Will split f_name to different values in a list from - 
# Output -> ['Earth ', ' Our Solar System ', ' #4'] ......... ['Venus ', ' Our Solar System ', ' #3']
# Note: This assumes each filename has EXACTLY 2 hyphens (splitting into exactly 3 parts).
# If any filename had an extra '-' in the title, this would raise a error.
# ValueError: too many values to unpack (expected 3)
# A safer version for messier filenames: f_name.split('-', maxsplit=2)

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 
    print(f_title) # Output -> Earth Jupiter .......... Uranus Venus
    print(f_course) # Output -> Our Solar System ......... Our Solar System
    print(f_num) # Output -> #4 #6 #5 ........ #9 #3

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 
    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
# Output -> #4- Our Solar System -Earth .mp4 .......... #3- Our Solar System -Venus .mp4

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 

    # Doing this will remove any wide spaces in starting or end ->
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()

    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
# Output -> #4-Our Solar System-Earth.mp4 .......... #3-Our Solar System-Venus.mp4

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:] # Leaving first character that is # and taking rest part.

    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
# Output -> 4-Our Solar System-Earth.mp4 .......... 3-Our Solar System-Venus.mp4

# Padding single digits with zero or else when we sort them 1 and 10 can be after each other instead of 1 and 2
for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 
# .zfill(number_of_digits) will padd numbers with zeros as per number_of_digits provided.
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    print('{}-{}-{}{}'.format(f_num, f_course, f_title, f_ext))
# Output -> 04-Our Solar System-Earth.mp4 .......... 03-Our Solar System-Venus.mp4

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    print('{}-{}{}'.format(f_num, f_title, f_ext))
# Output -> 04-Earth.mp4 .......... 03-Venus.mp4

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f) 
    f_title, f_course, f_num = f_name.split('-') 

    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)

    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)

    os.rename(f, new_name) # Will rename all files in directory.

'''
After renaming -> 

04-Earth.mp4
06-Jupiter.mp4
05-Mars.mp4
02-Mercury.mp4
08-Neptune.mp4
10-Pluto.mp4
07-Saturn.mp4
01-The Sun.mp4
09-Uranus.mp4
03-Venus.mp4
'''

'''
Since files are arranged in defult by accending order top - bottom
So final version will be ->

01-The Sun.mp4
02-Mercury.mp4
03-Venus.mp4
04-Earth.mp4
05-Mars.mp4
06-Jupiter.mp4
07-Saturn.mp4
08-Neptune.mp4
09-Uranus.mp4
10-Pluto.mp4
''' 
