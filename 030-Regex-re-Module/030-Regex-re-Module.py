# Here we will be learning how to read, write, and match regular expressions with the re module, Regular expressions are also called regax.
# Regular expressions are extremely useful for matching common patterns of text such as email addresses, phone numbers, URLs, etc.
# Learning how to do this within Python will allow us to quickly parse files and text for the information that we need.

import re

# Sample Multi line string to search ->
text_to_search ='''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] / | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# Raw String -> A string prefixed with an r which tells python not to handle back slashes in any special way.
print('\tTab') # Output ->         Tab
print(r'\tTab') # Output -> \tTab
# Raw string will interpret the string literally.

# To write patterns we can use re.compile() method.
# The compile method will allow us to seperate out our patterns into a variable and we can also use that variable to perform multiple searches.

pattern = re.compile(r'abc') # Patterns is created.
matches = pattern.finditer(text_to_search) # .finditer() method returns an iterator that contains all of the matches 

for match in matches: # matches will be an object in memory so looping it to see output.
    print(match)
# Output -> <re.Match object; span=(1, 4), match='abc'>
# The span is beginning and end index of the match
# when we searched this text with this pattern using the .finditer method it only found one match of ABC and it found it in our alphabet from indexes 1 to 4.
# We can use this indexes in string slicing in python to get the exact match from the searched string.
print(text_to_search[1:4]) # Output-> abc

pattern = re.compile(r'cba')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match) # Output ->
# If we searched something that is not present it will not give any out.

pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Doing this will search everything except \n

# So to search a literal period then we have to escape these characters with a backslash.
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match) 
# Output ->
# <re.Match object; span=(112, 113), match='.'>
# <re.Match object; span=(148, 149), match='.'>
# <re.Match object; span=(170, 171), match='.'>
# .
# .
# <re.Match object; span=(227, 228), match='.'>

pattern = re.compile(r'coreyms\.com')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output -> <re.Match object; span=(141, 152), match='coreyms.com'>

# Now let's use some regular expressions to match patterns or values ->

# Some meta characters and what they match -> 

# .       - Any Character Except New Line
# \d      - Digit (0-9) # Will match any digit from 0-9
# \D      - Not a Digit (0-9) # Will match anything that is not a digit
# \w      - Word Character (a-z, A-Z, 0-9, _) # Will match anything from a-z,A-Z,0-9,_
# \W      - Not a Word Character # Will anything except a-z,A-Z,0-9,_
# \s      - Whitespace (space, tab, newline) # Will match space, tab and newline
# \S      - Not Whitespace (space, tab, newline) # Will match anything except space, tab and newline

# Examples ->
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output -> 
# <re.Match object; span=(55, 56), match='1'>
# <re.Match object; span=(56, 57), match='2'>
# .
# .
# <re.Match object; span=(178, 179), match='4'>

pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(0, 1), match='\n'>
# <re.Match object; span=(1, 2), match='a'>
# .
# .
# <re.Match object; span=(230, 231), match='\n'>

pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='b'>
# .
# .
# <re.Match object; span=(229, 230), match='T'>

pattern = re.compile(r'\W')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(0, 1), match='\n'>
# <re.Match object; span=(27, 28), match='\n'>
# .
# .
# <re.Match object; span=(230, 231), match='\n'>

pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(0, 1), match='\n'>
# <re.Match object; span=(27, 28), match='\n'>
# .
# .
# <re.Match object; span=(230, 231), match='\n'>

pattern = re.compile(r'\S')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='b'>
# .
# .
# <re.Match object; span=(229, 230), match='T'>

# Below characters are called anchors.
# They don't match any characters but rather invisible positions before or after characters.
# We can use this in conjunction with other patterns for searching. 

# \b      - Word Boundary, word boundaries are indicated by whitespaces or a non-alphanumeric character.
# \B      - Not a Word Boundary
# ^       - Beginning of a String # Will match character if it's in beginning of a string
# $       - End of a String # Will match character if it's in ending of a string

pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Explanation =>Ha HaHa, here 3 Ha are there before first Ha there is a \n in upper line so it comes under word boundary,
# Before second Ha there is whitespace so it comes under word boundary but third Ha comes in middle of a word so its not in word boundary.  
# Output ->
# <re.Match object; span=(66, 68), match='Ha'>
# <re.Match object; span=(69, 71), match='Ha'>

# Will print that is not under word boundary.
pattern = re.compile(r'\BHa')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output -> 
# <re.Match object; span=(71, 73), match='Ha'>

pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches: 
    print(match)
# Output -> 
# <re.Match object; span=(0, 5), match='Start'>

# If we used caret ^ with a character that is in a string but not at beginning it will not match it and will not show any output.

pattern = re.compile(r'end$')
matches = pattern.finditer(sentence)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(41, 44), match='end'>

# If we used $ with a character that is in a string but not at ending it will not match it and will not show any output.

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(154, 166), match='321-555-4321'>
# <re.Match object; span=(167, 179), match='123.555.1234'>

# Some use full regular expressions for working with a long pattern.
# []      - Matches Characters in brackets and is called character set.
# [^ ]    - Matches Characters NOT in brackets

# [] -> Matches [c1 or c2] where c1 and c2 are any characters means if it find any one from c1 or c2 it will show that.
# [] -> Can contain many characters not only c1 and c2.
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(154, 166), match='321-555-4321'>
# <re.Match object; span=(167, 179), match='123.555.1234'>

pattern = re.compile(r'\d\d\d[-]\d\d\d[-]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(154, 166), match='321-555-4321'>

pattern = re.compile(r'[31]2[13][-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(154, 166), match='321-555-4321'>
# <re.Match object; span=(167, 179), match='123.555.1234'>

# - is also a special character and can be used between characters to find characters between given range.
# [c1-c2] will find characters from c1 to c2 individually.
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(55, 56), match='1'>
# <re.Match object; span=(56, 57), match='2'>
# .
# .
# <re.Match object; span=(178, 179), match='4'>

pattern = re.compile(r'[a-d]')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='b'>
# .
# .
# <re.Match object; span=(218, 219), match='b'>

pattern = re.compile(r'[a-dA-K]')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(1, 2), match='a'>
# .
# <re.Match object; span=(28, 29), match='A'>
# .
# <re.Match object; span=(218, 219), match='b'>

# With-in a character set caret ^ negates the set and matches everything that is not in character set.
pattern = re.compile(r'[^a-zA-Z]')
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(0, 1), match='\n'>
# <re.Match object; span=(27, 28), match='\n'>
# .
# <re.Match object; span=(228, 229), match=' '>
# <re.Match object; span=(230, 231), match='\n'>

example_string = '''
cat
mat
pat
bat
'''

pattern = re.compile(r'[^b]at')
matches = pattern.finditer(example_string)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(1, 4), match='cat'>
# <re.Match object; span=(5, 8), match='mat'>
# <re.Match object; span=(9, 12), match='pat'>

# We can use Quantifiers to match multiple character at a time ->
# Quantifiers:
# *       - Will match 0 or More of the pattern that we are looking for.
# +       - Will match 1 or More of the pattern that we are looking for.
# ?       - Will match 0 or 1 of the pattern that we are looking for.
# {3}     - Will match Exact Number of the pattern
# {3,4}   - Will match Range of Numbers (Minimum, Maximum)

# Examples ->
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(154, 166), match='321-555-4321'>
# <re.Match object; span=(167, 179), match='123.555.1234'>

pattern = re.compile(r'Mr\.') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(181, 184), match='Mr.'>
# <re.Match object; span=(225, 228), match='Mr.'>

pattern = re.compile(r'Mr\.?') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(181, 184), match='Mr.'>
# <re.Match object; span=(193, 195), match='Mr'>
# <re.Match object; span=(211, 213), match='Mr'>
# <re.Match object; span=(225, 228), match='Mr.'>

pattern = re.compile(r'Mr\.?\s[A-Z]') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(181, 186), match='Mr. S'>
# <re.Match object; span=(193, 197), match='Mr S'>
# <re.Match object; span=(225, 230), match='Mr. T'>

pattern = re.compile(r'Mr\.?\s[A-Z]\w+') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(181, 192), match='Mr. Schafer'>
# <re.Match object; span=(193, 201), match='Mr Smith'>

pattern = re.compile(r'Mr\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(181, 192), match='Mr. Schafer'>
# <re.Match object; span=(193, 201), match='Mr Smith'>
# <re.Match object; span=(225, 230), match='Mr. T'>

# Groups allow us to match several different patterns ->
# |       - Either Or
# ( )     - Group

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') 
matches = pattern.finditer(text_to_search)
for match in matches: 
    print(match)
# Output ->
# <re.Match object; span=(181, 192), match='Mr. Schafer'>
# <re.Match object; span=(193, 201), match='Mr Smith'>
# <re.Match object; span=(202, 210), match='Ms Davis'>
# <re.Match object; span=(211, 224), match='Mrs. Robinson'>
# <re.Match object; span=(225, 230), match='Mr. T'>


# Searching a different file using re module and context manager.
# Sample data.txt file used ->
'''
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com

Corey Jefferson
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com
.
.
.
Eric Stuart
952-555-3089
777 High St., King's Landing AZ 16547
johnstuart@bogusemail.com

Charles Miller
900-555-6426
207 Washington St., Blackwater MA 24886
charlesmiller@bogusemail.com
'''

# Searching all phone numbers in data.txt file.
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
with open('data.txt','r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

    for match in matches: 
        print(match)
# Output ->
# <re.Match object; span=(12, 24), match='615-555-7164'>
# <re.Match object; span=(102, 114), match='800-555-5669'>
# <re.Match object; span=(191, 203), match='560-555-5153'>
# .
# .
# <re.Match object; span=(8736, 8748), match='900-555-6426'>

pattern = re.compile(r'[31]2[13][-.]\d\d\d[-.]\d\d\d\d')
with open('data.txt','r') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches: 
        print(match)
# Output ->
# <re.Match object; span=(2645, 2657), match='321-555-9053'>


# Some Examples regarding emails ->

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>

pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
# <re.Match object; span=(25, 53), match='corey.schafer@university.edu'>

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
# <re.Match object; span=(25, 53), match='corey.schafer@university.edu'>
# <re.Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
# <re.Match object; span=(25, 53), match='corey.schafer@university.edu'>
# <re.Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>

# Let's see how to capture information from groups ->

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 13), match='https://www.'>
# <re.Match object; span=(24, 31), match='http://'>
# <re.Match object; span=(43, 51), match='https://'>
# <re.Match object; span=(63, 75), match='https://www.'>

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 23), match='https://www.google.com'>
# <re.Match object; span=(24, 42), match='http://coreyms.com'>
# <re.Match object; span=(43, 62), match='https://youtube.com'>
# <re.Match object; span=(63, 83), match='https://www.nasa.gov'>

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
# Output ->
# <re.Match object; span=(1, 23), match='https://www.google.com'>
# <re.Match object; span=(24, 42), match='http://coreyms.com'>
# <re.Match object; span=(43, 62), match='https://youtube.com'>
# <re.Match object; span=(63, 83), match='https://www.nasa.gov'>

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(0)) # .group(0) is the entire match
# Output ->
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(1))
# Output ->
# www.
# None
# None
# www.

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(2))
# Output ->
# google
# coreyms
# youtube
# nasa

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))
# Output ->
# .com
# .com
# .com
# .gov

# We can use .sub(r'Back references', String to search) method to perform substitution.
# Back refrences are used to refrence groups.
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls) # Returns a new string with substituted groups.
print(subbed_urls)
print(type(subbed_urls))
# Output ->

# google.com
# coreyms.com
# youtube.com
# nasa.gov

# <class 'str'>

# we have used .finditer() method till now as it shows all the matches and locations in easy understandable form.
# But there are some other methods all available for different purposes.

# .findall() method returns the matches as a list of string and if it's matching groups then it will only return groups.
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') 
matches = pattern.findall(text_to_search)
for match in matches: 
    print(match)
# Output -> # Only prints out first group.
# Mr
# Mr
# Ms
# Mrs
# Mr

# For multiple groups .findall() method will return a list of tuples and the tuples would contain all the groups.
# If there are no groups then it will return all the matches in a list of strings.
pattern = re.compile(r'\d{3}.\d{3}.\d{4}') 
matches = pattern.findall(text_to_search)
for match in matches: 
    print(match)
print(type(matches))
# Output -> 
# 321-555-4321
# 123.555.1234
# <class 'list'>

# Now let's see .match() method.
# It will determine if the regular expression matches at the beginning of the string.

# pattern = re.compile(r'Start') 
# matches = pattern.match(sentence)
# for match in matches: 
#     print(match)
# Output -> Will give error as match dosen't return an iterable.

# .match() method just returns the first match, if no match then it returns None.
# Only prints out first match.
pattern = re.compile(r'Start') 
matches = pattern.match(sentence)
print(matches)
# Output -> <re.Match object; span=(0, 5), match='Start'>

# .match() only search beginning of string,
# so if we searched something that is present but not at beginning it will return None.
pattern = re.compile(r'sentence') 
matches = pattern.match(sentence)
print(matches)
# Output -> None

# To search entire string for any pattern we can use .search() method.
# It only prints out the first match that it got.
pattern = re.compile(r'sentence') 
matches = pattern.search(sentence)
print(matches)
# Output -> <re.Match object; span=(8, 16), match='sentence'>

# If something dosen't exist it returns None.
pattern = re.compile(r'DNE') 
matches = pattern.search(sentence)
print(matches)
# Output -> None

# We can use flags to ignore cases.
pattern = re.compile(r'start', re.IGNORECASE) 
matches = pattern.search(sentence)
print(matches)
# Output -> <re.Match object; span=(0, 5), match='Start'>

pattern = re.compile(r'start', re.I) 
matches = pattern.search(sentence)
print(matches)
# Output -> <re.Match object; span=(0, 5), match='Start'>
