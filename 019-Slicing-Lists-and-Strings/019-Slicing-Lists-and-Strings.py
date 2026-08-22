my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_list)
# Output -> [0,1,2,3,4,5,6,7,8,9]

print(my_list[0])
# Output -> 0
print(my_list[5])
# Output -> 5

print(my_list[-1])
# Output -> 9
print(my_list[-10])
# Output -> 0

'''
We can use list[start:end:step] to do slicing of a list

start → where slicing begins
stop → where slicing ends (not included)
step → how many positions to move each time
Positive step → move forward
Negative step → move backward
Leaving a value blank lets Python choose the appropriate default
'''

print(my_list[0:5])
# Output -> [0,1,2,3,4]

print(my_list[0:6])
# Output -> [0,1,2,3,4,5]

print(my_list[3:8])
# Output -> [3,4,5,6,7]

print(my_list[-7:-2])
# Output -> [3,4,5,6,7]

print(my_list[1:-2])
# Output -> [1,2,3,4,5,6,7]

print(my_list[1:9])
# Output -> [1,2,3,4,5,6,7,8]

print(my_list[1:])
# Output -> [1,2,3,4,5,6,7,8,9]

print(my_list[5:])
# Output -> [5,6,7,8,9]

print(my_list[:-1])
# Output -> [0,1,2,3,4,5,6,7,8]

print(my_list[:]) # This can also be used to copy a list -> variable = list[:] 
# Output -> [0,1,2,3,4,5,6,7,8,9]

print(my_list[2:-1])
# Output -> [2,3,4,5,6,7,8]

# Step allow us to skip certain number of values.

print(my_list[2:-1:2])  
# Output -> [2,4,6,8]

print(my_list[2:-1:1])
# Output -> [2,3,4,5,6,7,8]

print(my_list[2:-1:-1])
# Output -> []
# starts at index 2 and has a negative step, so Python would need to move backward.
# But the stop position -1 refers to the last element (index 9), which is ahead of index 2. Therefore, the result is empty.

print(my_list[-1:2:-1])
# Output -> [9,8,7,6,5,4,3]

print(my_list[-2:1:-1])
# Output -> [8,7,6,5,4,3,2]

print(my_list[-2:1:-2])
# Output -> [8,6,4,2]

print(my_list[::-1])
# Output -> [9,8,7,6,5,4,3,2,1,0]

'''Slicing through string'''

sample_url = "http://coreyms.com"

print(sample_url)
# Output -> http://coreyms.com 

print(sample_url[::-1])
# Output -> moc.smyeroc//:ptth

print(sample_url[-4:])
# Output -> .com

print(sample_url[7:])
# Output -> coreyms.com

print(sample_url[7:-4])
# Output -> coreyms 
