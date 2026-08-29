# The OS Module allow us to interact with operating system.
# For example -> We can navigate file system, get file information.
#             -> Look up and change environment variables.
#             -> Move files to different locations etc.

import os # It is a built-in libary.

# print(dir(module_name)) shows all attributes and methods that we have access to within this module.
print(dir(os))

print(os.getcwd()) # Prints current working directory path.
# getcwd -> get current working directory.

# chdir -> change directory.
# r is used before name so full '' will be considered as path, means whatever we write in '' after writing r in front will be considered as path. 
os.chdir(r'New_directory_path') # Change current directory with new directory.
print(os.getcwd()) # Will print new directory path.

# To view files and folders on directory we can do ->
print(os.listdir('directory_path')) # Prints a list with all files and folders in current directory.
# If we don't pass directory_path it will show current working directory files and folders.

# To create a directory/folder in current directory we can do ->
os.mkdir('Folder_name')  
os.makedirs('Folder_name')
# Both creates a folder with given name in string.
# We use os.makedirs('foldername_out/foldername_in') to create folders inside a folder together.
# Where as os.mkdir('foldername_out/foldername_in') will give error because foldername_out is not yet created.
# So makedirs() can create both directories and sub directories together or alone where as mkdir() can not until outer directory is created.

# Deleting directories is also similar we have ->
os.rmdir('directory_name') # Will delete only specific directory which name we pass.
os.removedirs('directory_name') # Will also delete intermidate directories.

# Safest -> os.makedirs('directory') for creating.
#        -> os.rmdir('directory') for deleting.

# To rename file or folder in current directory we can do ->
os.rename('Project.py','Tick_Tak_project.py')
# os.rename('original_name','new_name')

# To view information about a file we can do ->
print(os.stat('Tick_Tak_project.py'))
# Output -> os.stat_result(st_mode=33206, st_ino=3940649673949819, st_dev=12736913265458342588, st_nlink=1,
#           st_uid=0, st_gid=0, st_size=2864, st_atime=1787944662, st_mtime=1784245104, st_ctime=1782874676)

# We can also get specific information.
print(os.stat('Tick_Tak_project.py').st_size) # Output -> 2864
# prints file size in bytes.

# Will print last modification time in time-stamp form.
print(os.stat('Tick_Tak_project.py').st_mtime) # Output -> 1784245104

# To convert timestamp into human readable form we can do ->
from datetime import datetime
mod_time = os.stat('Tick_Tak_project.py').st_mtime
print(datetime.fromtimestamp(mod_time)) # Output -> 2026-08-29 12:06:29.687474
# os.stat('Tick_Tak_project.py').st_atime will return a timestamp, we will store that in a variable.
# we will pass that variable in datetime.fromtimestamp(variable) this will convert timestamp to human readable form.

print("Accessed:", datetime.fromtimestamp(os.stat('Tick_Tak_project.py').st_atime))
print("Modified:", datetime.fromtimestamp(os.stat('Tick_Tak_project.py').st_mtime))
print("Created/Changed:", datetime.fromtimestamp(os.stat('Tick_Tak_project.py').st_ctime)) 
print("Created/Changed:", datetime.fromtimestamp(os.stat('Tick_Tak_project.py').st_birthtime))
# st_atime → last access (read)
# st_mtime → last modification (content changed)
# st_ctime -> deprecated for creation time; will mean "metadata change time" in future
# st_birthtime -> use this instead to get actual file creation time

# os.walk() is a generator that traverses the entire directory tree, starting from the given path.
# By default it walks top-down, meaning it starts at the given path and goes deeper into each subfolder one at a time.
# For each directory it visits, it yields a tuple of 3 values: (dirpath, dirnames, filenames)
#   -> dirpath   : the current folder path being walked.
#   -> dirnames  : list of sub-directories within that dirpath.
#   -> filenames : list of files within that dirpath.
# It keeps repeating this process, going deeper into each subdirectory, until it has walked through
# the entire tree of folders and files starting from the root path we gave it.
# This is extremely useful when we don't know exactly where a file is located within a directory structure,
# or when we want to collect file information (like in a web app) across an entire folder tree.
path = r'D:\1. Python Corey Schafer'
print("Exists:", os.path.exists(path)) # Will print True if path exist, else False.
for dirpath, dirnames, filenames in os.walk(path):
    print('Current Path:', dirpath)
    print('Directories:', dirnames) 
    print('Files:', filenames)
    print() 

# os.environ gives us access to all environment variables on our system as a dictionary-like object.
print(os.environ)
# Output -> environ({'USERNAME': 'YourName', 'OS': 'Windows_NT', 'PATH': 'C:\\Windows\\...', ...})

# We can get a specific environment variable using os.environ.get('VARIABLE_NAME').
# Here we're getting the 'Home' variable, which holds the path to the user's home directory.
print(os.environ.get('Home'))
# Output -> None
# Note: On Windows, there's no 'Home' variable by default. Use 'USERPROFILE' instead:
# os.environ.get('USERPROFILE') -> Output -> C:\Users\YourName

# Now let's say we want to create a new file inside our home directory.
# One way people try to do this is by simply concatenating strings together.
file_path = os.environ.get('Home') + 'test.test' 
print(file_path) 
# Output -> TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
# (since 'Home' returned None on Windows; if it returned a real path, output would look like:
#  C:\Users\YourNametest.test  <- notice missing slash, this is the bug being demonstrated)

# Problem -> This is unreliable because we have to manually remember to add a slash between the
# home path and filename. It's easy to forget the slash, or paths might already come with slashes
# at the end, leading to missing slashes or double slashes.

# To avoid this guesswork, we can use os.path.join() instead.
# os.path.join() properly combines two or more paths together and takes care of adding
# the correct slash automatically.
file_path = os.path.join(os.environ.get('Home'),'test.txt')
print(file_path) 
# Output -> C:\Users\YourName\test.txt   (slash added automatically)

# os.path.basename() -> gives us just the filename from a full path (doesn't have to actually exist).
print(os.path.basename('/temp/test.txt'))
# Output -> test.txt

# os.path.dirname() -> gives us just the directory portion of a full path.
print(os.path.dirname('/temp/test.txt')) 
# Output -> /temp

# os.path.split() -> gives us both the directory name and the base name together as a tuple.
# (directory_name, base_name)
print(os.path.split('/temp/test.txt')) 
# Output -> ('/temp', 'test.txt')

# os.path.exists() -> checks if a given path actually exists on the filesystem.
# Returns True if it exists, False if it doesn't.
print(os.path.exists('/temp/test.txt'))
# Output -> False   (this is a fake path that doesn't exist)

# os.path.isdir() -> returns True if the given path is a directory.
print(os.path.isdir('/tem/fgdfgdf'))
# Output -> False

# os.path.isfile() -> returns True if the given path is a file.
# Useful because sometimes temporary files might not have an extension, 
# so checking isdir/isfile helps confirm what type of path we're dealing with.
print(os.path.isfile('/tem/fgdfgdf'))
# Output -> False

# os.path.splitext() -> splits the path into (root, extension).
# Easier than manually slicing strings to separate a filename from its extension.
print(os.path.splitext('/tem/test.txt')) 
# Output -> ('/tem/test', '.txt')

# Just like the os module, we can print dir(os.path) to see all available 
# attributes and methods within the os.path module.
print(dir(os.path))
# Output -> ['__all__', '__builtins__', ..., 'basename', 'dirname', 'exists', 'isdir', 'isfile', 
#            'join', 'split', 'splitext', ...] 
