"""
-----------------------------------------------------------------------------------------------
Optimal Stopping Game
-----------------------------------------------------------------------------------------------
Created by Gianluca Capraro, August 2019
-----------------------------------------------------------------------------------------------
The purpose of this script is:

To allow users to try their hand at an interactive version of the optimal stopping problem: 
	- a series of random numbers is generated
	- numbers could fall between 1 and 10,000 (the actual range will be different each time)
	- begin by revealing one number and then continue revealing the next
		numbers until you believe you have reached greatest value in the set
	- the goal is to stop at the greatest number

In simulations of the optimal stopping problem, the strategy for the greatest chance of success
is to view roughly 37% of the numbers and to then choose the next number that is greater than
all previously observed values.
-----------------------------------------------------------------------------------------------
To play the game, simply run this script from the command line and follow the instructions.
-----------------------------------------------------------------------------------------------
"""
import numpy as np

print("\n\n\n\nWelcome to the Optimal Stopping Game.\n")

print("How to play:")
print("(1) In this game, your goal is to reveal numbers until you believe you have reached the greatest value in the set.")
print("(2) If you believe there is a higher number yet to be reached, you can continue to reveal numbers.")
print("(3) Each time you play, the range of values will be different, but overall, the max number will not exceed 10,000.")
print("(4) At the end of the game, the highest number will be revealed, and the accuracy of your choice is measured.\n")

#define function to get array size to generate
def getArraySize(message):
	while True:
		try:
			userInput = int(input(message))       
		except ValueError:
			print("Please enter an integer value.")
			continue
		else:
			if userInput >= 10:
				return userInput 
				break 
			else:
				print("Please enter a value greater than or equal to 10.")
				pass


n_to_gen = getArraySize("How many numbers would you like to generate for the game? (Value must be >= 10):  ")
print('\n')

#determine max possible number using np random within range
highest_num = np.random.randint(low = 1000, high = 10000, size = 1)[0]
"""
print("The highest number possible is: " + str(highest_num))
print('\n')
"""

#generate random array of numbers based on highest range and number that was specified
array_of_nums = np.random.randint(low = 1, high = highest_num, size = n_to_gen).tolist()
print(str(n_to_gen) + " numbers have been generated.")
"""
print("Generated Numbers: " + str(array_of_nums))
print('\n')
"""

"""
Set up the lists that will be used for playing the game.
Define the optimal choice and current indices for gameplay.
"""
current_index = 0
num_list = []
list_to_show = []
for index in array_of_nums:
	num_list.append(index)
	list_to_show.append("*")
print('\n')
optimal_choice = max(num_list)
user_stopping_choice = 0
user_stopping_index = 0

#Show the list with all numbers hidden
print(list_to_show)
print('\n')

reveal = input("Press ENTER to reveal the first number: ")
while reveal.lower() != "stop" and current_index != n_to_gen:
	list_to_show[current_index] = num_list[current_index]
	user_stopping_choice = list_to_show[current_index]
	user_stopping_index = current_index
	current_index +=1
	print(list_to_show)
	print('\n')
	reveal = input("Press ENTER to reveal the next number, or type 'STOP' if satisfied: ")
print('\n')

"""
Game Over, display the optimal choice.
"""
print("Game Over.")
print("Optimal stopping choice: " + str(optimal_choice))
print('\n')

"""
Display user's value at stop, check for closeness to max value.
"""
print("Your stopping choice: " + str(user_stopping_choice))
if optimal_choice == user_stopping_choice:
	print("Congratulations, you made the optimal pick!")
else:
	acc_of_choice = int((user_stopping_choice/optimal_choice)*100)
	print("You reached ~" + str(acc_of_choice) + "% of the optimal value.")
print('\n')

"""
Display index metrics, did they use the optimal stopping strategy?
That is, viewing ~37% of the values, and then choosing the next highest observed?
"""
print("You chose to stop at index: " + str(user_stopping_index))
stopping_percent = int((user_stopping_index/n_to_gen)*100)

if current_index == n_to_gen:
	print("You viewed all options before deciding to stop.")
else:
	print("You viewed ~" + str(stopping_percent) + "% of the total number of potential choices before stopping.")
print('\n')
