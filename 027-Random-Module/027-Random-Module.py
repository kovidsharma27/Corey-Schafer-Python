# Random module is a built-in module which can be used to get some random data 
# We can create random numbers and can grab random values from a list of values
# Note -> Random module should not be used for security purposes or cryptography as per mentioned in python documentation
#      -> Instead we can use secrets module if we are trying to do something related to security.

# Random module can be used to generate some random data or a game where we need some random values or shuffle some values.

import random 

# Let's look at random and uniform methods ->

# We can use the random method to get a random float value between 0 and 1 where 0 will be inclusive and 1 will be non-inclusive.
value = random.random()
print(value) # Output -> 0.8725495688410541
print(value) # Output -> 0.8725495688410541
# Writing different print statements will not work — 'value' was only assigned once,
# so it stays the same for every print until reassigned.

# Instead we have to execute/run program multiple times to get random values.
# (Below output is from re-running the ENTIRE script, not from this same execution — 
#  since value stays fixed within one run, only a fresh run generates a new random number for it.)
print(value) # Output -> 0.13138784874136888
print(random.random()) # A fresh call to random.random() itself WILL differ every time, even within the same run.

# variable = random.random() is not much useful as it only gives random float values between 0 and 1
# We can multiple this random.random() with certain values to get random values in range.
value = random.random()
# Will give random float values between 0 - 2
print(value*2) # Output -> 1.9876486251767558
# But there are certain better ways to do this.

# We can use .uniform() method to get a random value between certain range.
value = random.uniform(1, 10) # Will give random float values between 1-10 where 1 is inclusive and 10 is non-inclusive.
print(value) # Output -> 8.66410163812835

# To get random whole number or integers we can use .randint(lower_bound, upper_bound) method where both lower_bound and upper_bound will be inclusive.
value = random.randint(1,6) # This example can be used to simulate dice roll.
print(value) # Output -> 5

value = random.randint(0,1) # This example can be used to simulate coin toss.
print(value) # Output -> 0

# We can also use .choice(list) method to get a random value from a list of values.
greetings = ['hello', 'Hi', 'hey', 'Howdy', 'Hola']
value = random.choice(greetings) # Will pick a random value from greetings list.
print(value + ', Corey!') # Output -> Hola, Corey!

# It's also possible to get multiple random values from a list.
# To get multiple random values we can use .choices(list, k = no.of_random_values) method instead of .choice(list) method.
# It will give multiple random values in a list.
colors = ['Red', 'Black', 'Green']
results = random.choices(colors, k = 10) # Here k is how many times we want a random value.
print(results) # Output -> ['Black', 'Red', 'Black', 'Red', 'Black', 'Red', 'Red', 'Green', 'Black', 'Green']

# Above methods give a random value, where all values are equally likely to occur.

# But we can weights certain values to make our random values not equally likely.
colors = ['Red', 'Black', 'Green']
results = random.choices(colors, weights = [18, 18, 2], k = 10) # Now random values are not equally likely.
# For this example -> Total chances = 38
#                  -> Red = 18/38 chnace , Black = 18/38 chance, Green = 2/38 chance.
#  So green is less likely to occur as compared to other values.
print(results) # Output -> ['Red', 'Red', 'Black', 'Black', 'Red', 'Red', 'Red', 'Black', 'Black', 'Green']

# Now let's ramdomly shuffle list of values ->
deck = list(range(1, 53))
print(deck) 
# Output -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 
#           28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]

# Now to shuffle list of values we can use random.shuffle(list) and this don't create a new variable instead modify the original list.
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)
# Output -> [13, 5, 42, 3, 24, 17, 15, 14, 35, 37, 46, 29, 11, 34, 16, 43, 9, 18, 25, 19, 28, 27, 30, 8, 52, 26,
#            47, 21, 31, 41, 6, 2, 51, 50, 40, 23, 36, 1, 4, 22, 48, 20, 7, 12, 33, 39, 32, 10, 45, 38, 49, 44]

# Now let's say that we wanted to get 5 random value from this deck now we can use the choices method, 
# but this wouldn't really work because with the choices method it could randomly grab the same cards multiple times, 
# so for example it could randomly select any one card multiple times but we only want unique cards, 
# so to do this we're going to use the sample method now it'll make sure that it only grabs unique cards from our sequence

# In short -> choices method => multiple random values but duplicates can occur.
#             sample method => multiple random and unique values.
 
deck = list(range(1, 53))
hand = random.sample(deck, k = 5)
print(hand) # Output -> [47, 3, 40, 50, 12]

# Now let's see practical use case for what we have learned ->

'''We will be creating fake names, phone_numbers, addresses and emails'''
'''Some random data for our practical'''

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 
               'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 
              'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 
              'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 
               'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 
               'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 
          'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 
          'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100): # We will create 100 fake datas.
    first = random.choice(first_names) # random first name from first_names will be selected 
    last = random.choice(last_names) # random last name from last_names will be selected 

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}' # Using a f string to create a random phone number.
    # random number from 100-999 then 555 then random number from 1000-9999

    street_num = random.randint(100, 999) # Random street number from 100-999
    street = random.choice(street_names) # Random street name from street_names
    city = random.choice(fake_cities) # Random city from fake_cities
    state = random.choice(states) # Random state from states
    zip_code = random.randint(10000, 99999) # Random zip code from 10000-99999
    address = f'{street_num} {street} St., {city} {state} {zip_code}' # creating address with f string

    email = first.lower() + last.lower() + '@bogusemail.com' # Creating random email

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
# Output ->
# Jennifer Williams
# 270-555-9989
# 206 High St., Sunnydale OH 88961
# jenniferwilliams@bogusemail.com

# Mary Taylor
# 390-555-7062
# 495 Pine St., King's Landing IL 36006
# marytaylor@bogusemail.com

# Barbara Arnold
# 975-555-8294
# 610 Pine St., Oldtown IL 22777
# barbaraarnold@bogusemail.com

# .
# .
# .
# .
# .

# Tom Wilson
# 499-555-7671
# 285 Lake St., King's Landing WA 58828
# tomwilson@bogusemail.com

# Charles Jones
# 914-555-2145
# 324 Elm St., Olympus KY 89747
# charlesjones@bogusemail.com 

#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node* next;
};

struct node* createnode(int val)
{
    struct node* new_node = malloc(sizeof(struct node));
    new_node -> data = val;
    new_node -> next = NULL;

    return new_node;
}

void display(struct node* head)
{
    struct node* temp = head;
    while(temp!=NULL)
    {
        printf("%d -> ",temp -> data);
        temp = temp -> next;
    }
    printf("\n");
}

int main()
{
    struct node* head = createnode(10);
    head -> next = createnode(20);
    head -> next -> next = createnode(30);

    display(head);

    return 0;
} 
