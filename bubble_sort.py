# Generate a list of 100 random numbers between 0 and 10000. Use bubble sort algorithm to 
# sort numbers from left to right
print "\n Creating and printing (unsorted) list of 100 random numbers between 0 and 10000: \n"

# Import random and datetime library to generate random numbers and allow time measurement
from random import randint
from datetime import datetime

# Timestamp beginning of program
start_time = datetime.now()

# Create empty list
bub_list = []

# Loop through 100 times to create the list, then print it
for num in range(0,100):
	rand = randint(0,10000)
	bub_list.append(rand)
print bub_list

# Line break and tell user that ordered list is now printing

print "\n Now printing sorted list: \n"

# Loop through the list created above 99 times (1 less than total length) from 99 to 0
# stepping down by 1
for char in range(len(bub_list)-1, 0, -1):

# Check each element in the list beginning with the left-most, each time checking the element
# to the right of it in the index to see which is larger. If the left element is larger, move
# it to the right. Check again until the largest number is inserted at the right end of the list
	for num in range(char):
		if bub_list[num] > bub_list[num + 1]:
			temp = bub_list[num]
			bub_list[num] = bub_list[num + 1]
			bub_list[num + 1] = temp

# print "\n Printing sorted list: \n"
print bub_list

# Timestamp end of program, subtract start from finish, print total in seconds
end_time = datetime.now()
total_time = end_time - start_time
print str(total_time.total_seconds()) + " seconds to run the command."