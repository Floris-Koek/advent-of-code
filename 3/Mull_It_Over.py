# Import regex
import re

# Define the pattern
mulpattern = r"mul\(\d+,\d+\)"

# Open and read the file
with open('input.txt') as file:
    # Read the content of the file into a single string
    content = file.read()

# Find all matches in the content
matches = re.findall(mulpattern, content)

# Pattern to match content between ( and ,
firstDigitPatern = r"\(([^,]+),"

# Pattern to match content between , and )
secondDigitPatern = r",([^)]+)\)"

totalSum = 0
for mul in matches:
    # print(mul)
    firstDigit = re.findall(firstDigitPatern, mul)
    secondDigit = re.findall(secondDigitPatern, mul)
    # print(firstDigit)
    # print(secondDigit)

     # Convert the extracted digits to integers
    firstDigit = int(firstDigit[0])
    secondDigit = int(secondDigit[0])

    # Multiply and add to the total sum
    totalSum += firstDigit * secondDigit

print(totalSum)