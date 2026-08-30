# File Objects are used to interact with files,
# there are many things that we can do with files within python. 

# To get a file object we can use built-in -> open <- command
# variable = open('file_path','mode') doing this will open the file in memory not in our screen.
# Since test.txt is in same directory as current file we can just pass name of the file that we want to open.
# variable = open('file_path') If we don't specify mode it will default open it as read(r) mode.
# File objects mode can be -> reading(r), writing(w), appending(a), reading and writing(r+)
f = open('test.txt',"r")
print(f.name) # prints name of opened file => Output -> test.txt 
print(f.mode) # prints mode in which file is opened => Output -> r
f.close() # In this method we have to close the opened file to free occupy space.
# Above method is not the preferable method to open any file as we have to manually close it.
# If we forget to close that it will take unnecessary space and leeks in memory.

# So preferable method is to use a context manager.
# We can use context manager by using -> with <- keyword.
# with open('file_path','mode') as variable_name: -> this will create a block.
# We can work/interact with files under that block and when we leave that block opened file will automatically be closed. 
with open('test.txt','r') as f:
    pass
# Even when we leave that block we will still be having access to that variable_name that we used to open file.
# In short after exiting block file will be closed but we can access context manager file variable.
print(f.closed) # Shows file is closed or not => Output -> True
# We just have access to variable_name, file will be closed so we can not read or write anything.
print(f.read()) # Output -> ValueError: I/O operation on closed file.

with open('test.txt','r') as f:
    f_contents = f.read()
    print(f_contents) # will print what is inside that opened file => Output -> 1) This is a test file! ........... 10) Tenth line
# For a small file this can work,
# but for very large file it will take a lot of space as doing this loads full file in memory then show it's contents.

# There are some other methods to read file contents instead of .read() method

with open('test.txt','r') as f:
    f_contents = f.readlines()
    print(f_contents) # Will print a list containing contents of that file.
# Output -> ['1) This is a test file!\n', '2) With miltiple lines of data...\n', ............... , '10) Tenth line\n']

with open('test.txt','r') as f:
    f_contents = f.readline() 
    print(f_contents) # Will print first line of opened file
# Output -> 1) This is a test file!

# Every time we run this it will give next line of our file.
with open('test.txt','r') as f:
    f_contents = f.readline() 
    print(f_contents) 

    f_contents = f.readline() 
    print(f_contents) 
# Output -> 1) This is a test file!

#           2) With miltiple lines of data...
# This extra new line came in between print statement by default adds a new line after executing.

# Doing this will not add new line after execution of print statement 
with open('test.txt','r') as f:
    f_contents = f.readline() 
    print(f_contents, end = '') 

    f_contents = f.readline() 
    print(f_contents, end = '') 
# Output -> 1) This is a test file!
#           2) With miltiple lines of data...

# To read a larger file we can iterate the lines in a file, as this will take one line in memory at a time.
with open('test.txt','r') as f:
    for line in f:
        print(line,end = '')
# Output -> 1) This is a test file! ........... 10) Tenth line

# With .read(date_amount) we can specify the amount of data that we want to read at a time,
# by passing in the size as an argument 
with open('test.txt','r') as f:
    f_contents = f.read(100) # Takes first 100 characters of file.
    print(f_contents, end = '') 
# Output -> 1) This is a test file! ...... 5) Fifth line

with open('test.txt','r') as f:
    f_contents = f.read(100) # Took first 100 characters
    print(f_contents, end = '')
    f_contents = f.read(100) # Took 100 characters after first 100 characters
    print(f_contents, end = '')
# Output -> 1) This is a test file! .......... 10) Tenth line

# If we reached end of contents then it will print rest as empty string.
with open('test.txt','r') as f:
    f_contents = f.read(100) 
    print(f_contents, end = '')
    f_contents = f.read(100) 
    print(f_contents, end = '')
    f_contents = f.read(100) 
    print(f_contents, end = '')
# Output -> 1) This is a test file! .......... 10) Tenth line

# Now to view content of a very large file we can combine loop with .read(data_chunks) 
with open('test.txt','r') as f:
    size_to_read = 100 # chunk_size of content to read at a time 
    f_contents = f.read(size_to_read) # passing chunk_size to file_name.read(chunk_size) and storing in a variable

    while len(f_contents) > 0: # Checks if f_contents is empty or not
        print(f_contents,end='') # rints chunk_content per looping
        f_contents = f.read(size_to_read) # again pass the content chunk_size
# If there will be no content left to loop in file,
# then it will return empty string so chunk_size will be 0 so looping will be stopped,
# as while loop checks chunk_size before very iteration.
# Output -> 1) This is a test file! ........... 10) Tenth line

# Did this to see how looping is done for each 10 character chunks as after each 10 characters * will be printed.
with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read) 

    while len(f_contents) > 0: 
        print(f_contents,end='*') 
        f_contents = f.read(size_to_read)
# Output -> 1) This is* a test fi*le! 2) Wit*h miltiple* lines of *data... 3)* Third lin*e ...... *10) Tenth *line *

with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read) 
    print(f.tell()) # Tells which position we are currently in our file # Output -> 10
# Note: f.tell() returns the byte position, not character position.
# For plain ASCII text these match, but for files with multi-byte characters (like emojis or non-English text),
# tell() and read() character counts can differ.

with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell()) # Output -> 10
    f_contents = f.read(size_to_read)
    print(f.tell()) # Output -> 20

with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents,end = '') # Will print first 10 characters 
    f_contents = f.read(size_to_read)
    print(f_contents,) # Will print next 10 characters
# Output -> 1) This is a test fi
# We do this for continuations of characters after end of a chunk

# But suppose we don't want to get next characters after a chank instead start again from satrting of chunk,
# So to do this we can use f.seek(position) to start from a perticular position
with open('test.txt','r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents,end = '') # prints first 10 characters
    f.seek(0) # Set position back to starting
    f_contents = f.read(size_to_read)
    print(f_contents,end = '') # prints first 10 characters from starting
# Output -> 1) This is1) This is

'''Now let's look at Writing a File'''

# Suppose we are in reading mode and we try to write something in reading mode, then this will happen ->
with open('test.txt','r') as f:
    f.write('Test') 
# Error will occur => Output -> io.UnsupportedOperation: not writable

# Let's create a new file called test2.txt in writing mode.
with open('test2.txt','w') as f:
    f.write('Test') 
# Now we don't have test2.txt in our directory, so if a file don't exist then it will create it.
# If a file exist then it will overwrite it, so we should be careful while working with writing mode

# If we want to work with a existing file without overwriting it then we can use appending(a) in mode.
with open('test2.txt','w') as f:
    pass

with open('test2.txt','a') as f:
    f.write('AppendedText')
# 'a' mode writes at the END of existing content instead of erasing it.
# If the file doesn't exist yet, 'a' mode will create it (same as 'w').

with open('test2.txt','w') as f:
    pass
# This will also create a test2.txt and since we are not writing anything in block, created file will be blank
# Means we don't necessary mean to write anything to create a file.

with open('test2.txt','w') as f: # After running this it will create a file named test2.txt in same directory
    f.write('Test') # And will write Test in it.
# Output -> test2.txt => Test

# same as read statements, file.write() then again file.write() will continue after first file.write() ended
with open('test2.txt','w') as f: 
    f.write('Test')
    f.write('Test')
# Output -> test2.txt => TestTest 

# We can also use file.seek(position) to write from a perticular position.
with open('test2.txt','w') as f: 
    f.write('Test') # Will write Test in test2.txt 
    f.seek(0) # Will set position back to starting
    f.write('R') # Will write R in sarting
# Output -> Rest
# (write('Test') → 'Test', then seek(0) resets cursor to start, then write('R')
#  overwrites only the first character 'T' with 'R', giving 'Rest')

'''
test.txt contents ->
1) This is a test file!
2) With miltiple lines of data...
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Ninth line
10) Tenth line

test2.txt contents ->
Test -> TestTest -> Rest
'''

'''Now let's combine everything'''
# We are going to create a copy of test.txt file ->

with open('test.txt','r') as rf: # We can write both of this write statements in one line seperated by commas,
    with open('test_copy.txt','w') as wf: # But for readability we are writing them seperate.
        for line in rf:
            wf.write(line)
# opened test.txt file as rf in read mode, opened/created test_copy.txt file as wf in write mode,
# looping through each line in rf and writing that in wf file.
# This will create a test_copy.txt file with same contents as test.txt

'''
test.txt contents ->
1) This is a test file!
2) With miltiple lines of data...
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Ninth line
10) Tenth line

test_copy.txt contents ->
1) This is a test file!
2) With miltiple lines of data...
3) Third line
4) Fourth line
5) Fifth line
6) Sixth line
7) Seventh line
8) Eighth line
9) Ninth line
10) Tenth line
'''

# Now let's do something similar but with a picture file not txt file.
with open('wallpaper.jpeg','r') as rf:
    with open('wallpaper_copy.jpeg','w') as wf:
        for line in rf:
            wf.write(line)
# Output -> UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 271: character maps to <undefined>
  
# So in order to work with image we have to open these files in binary mode
# Means we will be reading and writing bytes instead of working with text.

# For images => r -> rb | w -> wb
with open('wallpaper.jpeg','rb') as rf:
    with open('wallpaper_copy.jpeg','wb') as wf:
        for line in rf:
            wf.write(line)
# This will copy one image file to another image file.

# Instead of looping line by line we can also use chunks as we used in r mode
with open('wallpaper.jpeg','rb') as rf:
    with open('wallpaper_copy.jpeg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size) 
# This will copy one image file to another image file by using chunks instead of line by line.
