# Take int input from user, and loop through that number of times over sequence
# Step 1: Take input from user
# Step 2: Loop print sequence equal to length of user input
# Step 3: Use modifiers
# https://github.com/1thorarinn/sequence.git

n = int(input("Enter the length of the sequence: ")) # Do not change this line

# modifiers
first = 1
second = 2
third = 3
for i in range(1, n + 1) : 
    if i == 0:
        current = 0
    elif i == 1:
        current = 1
    elif i == 2:
        current = 2
    elif i == 3:
        current = 3    
    else :
        current = first + second + third
        first = second 
        second = third 
        third = current
    print(current) 