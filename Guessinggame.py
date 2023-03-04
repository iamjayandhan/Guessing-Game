# Step 1   - printing for display
print("G U E S S I N G    G A M E")
print("--------------------------")
print("Please think of a number (between 1 and 100) ")

# Step 2  - interactivity, getting input from user
input("Press enter when you are ready!...")

# Step 3 - conditionals
guess = 1 
print ("Is it", guess, "?")
resp = input("Is it correct? (Higher/H, Lower/L or yes) ")
if resp in ['yes', 'Yes', 'Y', 'y']:
	print("Number in 1 tries!")

count = 1

from fastguess import guesser, fguesser 

# Step 4 and Step 5 - Loops and functions 
while resp not in ['yes', 'Yes', 'Y', 'y']:
	count += 1
	
	# guess = guesser()
	guess = fguesser(resp)
	print ("Is it", guess, "?")
	resp = input("Is it correct? (H, L or yes) ")
	if resp in ['yes', 'Yes', 'Y', 'y']:
		print("Number of tries:", count)
		
    

print("Thank you for playing!")
