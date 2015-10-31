# Import necessary libraries
from random import randint
from datetime import datetime

# Timestamp start time of program

start_time = datetime.now()

# Create new list, populate it with 100 random numbers between 0 and 10000,
# then print the unsorted list

selection = []

for num in range(0, 100):
	rand = randint(0, 10000)
	selection.append(rand)
print selection

print "\n\n"

# Loop through the list created above 99 times (1 less than total length) from 99 to 0
# stepping down by 1, set a variable "smallest" equal to 0

for char in range(len(selection) -1, 0, -1):
	smallest = 0

# Take the first element and compare it to the next element to its right and move smaller
# to the right. Repeat for all elements in list. Once complete, set that element (which will
# be the smallest element in the list) as the first index in the list. Repeat to find next
# smallest until sorted in order left to right.

	for num in range(1, char + 1):
		if selection[num] > selection[smallest]:
			smallest = num
	temp = selection[char]
	selection[char] = selection[smallest]
	selection[smallest] = temp

# Print the newly sorted list

print selection

# Timestamp end of program, subtract start from finish, print total in seconds.

end_time = datetime.now()
total_time = end_time - start_time
print str(total_time.total_seconds())