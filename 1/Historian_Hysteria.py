# -----------------------
# OLD
# -----------------------

# Open and read the file
# numbers = open("numbers.txt", "r")
# print(numbers.read())

# # Initialize lists
# leftList = []
# rightList = []

# for line in numbers:
#      # Strip any extra whitespace and convert to an integer
#     number = int(line.strip())

#     if number % 2 == 0:
#         leftList.append(number)
#     else:
#         rightList.append(number)

# # Close the file
# numbers.close()

# with open("numbers.txt", "r") as numbers:
#     all_numbers = numbers.read().split()  # Split by whitespace
#     all_numbers = [int(num) for num in all_numbers]  # Convert to integers

# leftList = [num for num in all_numbers if num % 2 == 0]
# rightList = [num for num in all_numbers if num % 2 != 0]

# # Initialise variables
# totalDifference = 0

# # Set the number of loops to the length of the shorter list
# listLength = min(len(leftList), len(rightList))
# print("List length (iterations):", listLength)

# # Loop for total length of the shorter list
# for i in range(listLength):
#     # Get the smallest number from each list
#     lowestLeft = min(leftList)
#     lowestRight = min(rightList)

#     # Compare values and add the absolute difference to totalDifference
#     totalDifference += abs(lowestRight - lowestLeft)

#     # Remove the smallest numbers from their respective lists
#     leftList.remove(lowestLeft)
#     rightList.remove(lowestRight)

# # Print the final total difference
# print("Total Difference:", totalDifference)

# -----------------------
# General loading in TXT file
# -----------------------

# Load the data from the uploaded file
file_path = "numbers.txt"

# Read and process the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Extract the two lists from the lines, splitting by whitespace
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Sort both lists
left_list.sort()
right_list.sort()
# -----------------------
# DAY 1
# -----------------------
'''

# Calculate the total distance by pairing smallest elements
total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

print(total_distance)
'''
# -----------------------
# DAY 2
# -----------------------

# For every item in left list:
    # for item, repeat for every item in right list
        # compare item to every item in right list
        # if equal, up counter
        # at end, do left list item * counter and save to totalValue

totalValue = 0
for i in left_list:
    counter = 0
    for j in right_list:
        if i == j:
            counter +=1
        j+1
        i+1
    totalValue += i*counter
print(totalValue)