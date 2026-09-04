# In this module we will be looking at how to read parse and write CSV Files, CSV stands for Comma Separated values.
# CSV Files allow us to put some data in a plain test file and use some type of delimiter that seperates different fields.
# Usually a comma is used to seperate different fields.
# CSV Files are not structured for readability instead they are used to store large ammount of data.
# We can use our programs to parse out the desired information that we want from a CSV File.
# Generally in top of csv file fields are given that gives idea about what information we can expect from each line.
# The thing that seperates different fields/values is called a delimiter. A delimiter can be anything.
# For example a delimiter can be tab delimited values or dash or slash or underscore etc but they are all called CSV Files.

'''
Sample CSV File used ->

first_name,last_name,email
John,Doe,john-doe@bogusemail.com
Mary,Smith-Robinson,maryjacobs@bogusemail.com
Dave,Smith,davesmith@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Tom,Wright,tomwright@bogusemail.com
Steve,Robinson,steverobinson@bogusemail.com
Nicole,Jacobs,nicolejacobs@bogusemail.com
Jane,Wright,janewright@bogusemail.com
Jane,Doe,janedoe@bogusemail.com
Kurt,Wright,kurtwright@bogusemail.com
Kurt,Robinson,kurtrobinson@bogusemail.com
Jane,Jenkins,janejenkins@bogusemail.com
Neil,Robinson,neilrobinson@bogusemail.com
Tom,Patterson,tompatterson@bogusemail.com
Sam,Jenkins,samjenkins@bogusemail.com
Steve,Stuart,stevestuart@bogusemail.com
Maggie,Patterson,maggiepatterson@bogusemail.com
Maggie,Stuart,maggiestuart@bogusemail.com
Jane,Doe,janedoe@bogusemail.com
Steve,Patterson,stevepatterson@bogusemail.com
Dave,Smith,davesmith@bogusemail.com
Sam,Wilks,samwilks@bogusemail.com
Kurt,Jefferson,kurtjefferson@bogusemail.com
Sam,Stuart,samstuart@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Dave,Davis,davedavis@bogusemail.com
Sam,Patterson,sampatterson@bogusemail.com
Tom,Jefferson,tomjefferson@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Maggie,Jefferson,maggiejefferson@bogusemail.com
Mary,Wilks,marywilks@bogusemail.com
Neil,Patterson,neilpatterson@bogusemail.com
Corey,Davis,coreydavis@bogusemail.com
Steve,Jacobs,stevejacobs@bogusemail.com
Jane,Jenkins,janejenkins@bogusemail.com
John,Jacobs,johnjacobs@bogusemail.com
Neil,Smith,neilsmith@bogusemail.com
Corey,Wilks,coreywilks@bogusemail.com
Corey,Smith,coreysmith@bogusemail.com
Mary,Patterson,marypatterson@bogusemail.com
Jane,Stuart,janestuart@bogusemail.com
Travis,Arnold,travisarnold@bogusemail.com
John,Robinson,johnrobinson@bogusemail.com
Travis,Arnold,travisarnold@bogusemail.com
'''

import csv # In-built python module which helps to work with csv files.

with open('names.csv', 'r') as csv_file: # names.csv is in same directory, so just using file name instead of file path.
    csv_reader = csv.reader(csv_file) # we can use variable = csv.reader(opened_csv_file) method to seperate different fields.
# It seperates different fields and return them in a list. 
# In the background reader method is using a dialect that has some pre-set parameters for what it expects from a csv file.
# By default it expects values to be seperated by a comma and few other things.
# Since our sample csv file is simple we currently don't need to pass any additional parameter to reader method.

# csv_reader that we created is just any object in memory so we have to loop over it to view data.
    for line in csv_reader:
        print(line)
# Output -> 
# ['first_name', 'last_name', 'email'] 
# ['John', 'Doe', 'john-doe@bogusemail.com']
# .
# .
# .
# ['Travis', 'Arnold', 'travisarnold@bogusemail.com']

# since it's a list we can use all list methods to view it
with open('names.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
            print(line[2]) # Will give all emails as email field is currently in index 2.
# Output ->
# email
# john-doe@bogusemail.com
# .
# .
# .
# travisarnold@bogusemail.com

with open('names.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # next() is a built-in function that returns the next item from an iterator,
    # by calling that iterator's __next__() method internally.
    # Here, csv_reader is an iterator, so next(csv_reader) advances past the header row (field names),
    # leaving the loop below to start from the first actual data row.
    # Here it will skip that first value that is email field and return everything after it.
    for line in csv_reader:
            print(line[2])
# Output -> 
# john-doe@bogusemail.com
# maryjacobs@bogusemail.com
# .
# .
# .
# travisarnold@bogusemail.com

# Writing in csv file -> 

# This will create a new_csv file with data of our old csv_file and will use "-" as a delimiter instead of comma.
# If file name already exist it will over write it.
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file: 
        csv_writer = csv.writer(new_file, delimiter = '-') # If we don't pass delimiter it will consider comma as default.

        for line in csv_reader:
            csv_writer.writerow(line)

# we are opening the original csv file to be read and then we're creating this csv_reader variable and we are using the csv.reader() method 
# To read that original CSV file and then we're opening a new file for writing called new_names.csv and then we're creating a csv_writer variable,
# and we're using this csv.writer() method of the CSV module to open up a writer using that new file with a delimiter of a dash 
# and then for each line in this original CSV data we are writing out to the new file each line of the original file.

# Output -> Created new_names.csv with data ->
# first_name-last_name-email

# John-Doe-"john-doe@bogusemail.com"

# Mary-"Smith-Robinson"-maryjacobs@bogusemail.com

# .
# .
# .

# Travis-Arnold-travisarnold@bogusemail.com 

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file: 
    # newline='' prevents Python's automatic newline translation (which converts \n to \r\n on Windows).
    # csv.writer already adds its own \r\n line terminator — without newline='', the two combine
    # and create an extra blank line after every row. Always use newline='' when writing CSV files.
        csv_writer = csv.writer(new_file, delimiter = '-') # If we don't pass delimiter it will consider comma as default.

        for line in csv_reader:
            csv_writer.writerow(line)
# Output -> 
# first_name-last_name-email
# John-Doe-"john-doe@bogusemail.com"
# Mary-"Smith-Robinson"-maryjacobs@bogusemail.com
# .
# .
# .
# Travis-Arnold-travisarnold@bogusemail.com 

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t') 

        for line in csv_reader:
            csv_writer.writerow(line)
# Output -> Created new_names.csv with data ->
# first_name	last_name	email
# John	Doe	john-doe@bogusemail.com
# Mary	Smith-Robinson	maryjacobs@bogusemail.com
# .
# .
# .
# Travis	Arnold	travisarnold@bogusemail.com 

with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) 
    for line in csv_reader:
        print(line)
# Output -> In new_names.csv delimiter is \t not default comma and we didn't specify delimiter so it dosen't know how to seperate values.
# ['first_name\tlast_name\temail']
# ['John\tDoe\tjohn-doe@bogusemail.com']
# ['Mary\tSmith-Robinson\tmaryjacobs@bogusemail.com']
# .
# .
# .
# ['Travis\tArnold\ttravisarnold@bogusemail.com ']

with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t') 
    for line in csv_reader:
        print(line)
# Output ->
# ['first_name', 'last_name', 'email']
# ['John', 'Doe', 'john-doe@bogusemail.com']
# ['Mary', 'Smith-Robinson', 'maryjacobs@bogusemail.com']
# .
# .
# .
# ['Travis', 'Arnold', 'travisarnold@bogusemail.com ']

# We can also use DictReader and DictWriter instead of reader and writer method ->
# Using DictReader and DictWriter make it more easy and understandable what we are trying to do.

# Gives a dictionary as fields as key and data as value for each line/value.
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line) 
# Output ->
# {'first_name': 'John', 'last_name': 'Doe', 'email': 'john-doe@bogusemail.com'}
# {'first_name': 'Mary', 'last_name': 'Smith-Robinson', 'email': 'maryjacobs@bogusemail.com'}
# .
# .
# .
# {'first_name': 'Travis', 'last_name': 'Arnold', 'email': 'travisarnold@bogusemail.com '}

# Dictionary reader make it easier to parse out information.
# For example -> When working with csv.reader() we have to pass index of a fieled to get only that field data.
#                But suppose if we don't know the index of that field then we have to look csv file and find index.
#                This can be very difficult for csv files with large number of fields.
# So, by using csv.DictReader() method we just have to pass field name instead of index in print statement as fields are now keys.

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line['email'])
# Output -> 
# john-doe@bogusemail.com
# maryjacobs@bogusemail.com
# .
# .
# .
# travisarnold@bogusemail.com

# Now let's look at how to use dictionary writer -> csv.DictWriter()
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader() # We can use this to get field name also with data.

        for line in csv_reader:
            csv_writer.writerow(line) 
# Output -> first_name	last_name	email
# John	Doe	john-doe@bogusemail.com
# Mary	Smith-Robinson	maryjacobs@bogusemail.com
# .
# .
# .
# Travis	Arnold	travisarnold@bogusemail.com 

# Suppose we wanted only few fields data instead of all, so with writer() we have to pass index in writerow()
# But with Dictwriter we can do this ->
with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader() # We can use this to get field name also with data.

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line) 
# Output ->
# first_name	last_name
# John	Doe
# Mary	Smith-Robinson
# .
# .
# .
# Travis	Arnold 
