# def isAscending(line):
#     try:
#         numbers = list(map(int, line.split()))
#         # Check if the list is sorted in ascending order, also check if by at least one but not more than 3
#         return all(1 <= numbers[i+1] - numbers[i] <= 3 for i in range(len(numbers) - 1))
#     except ValueError:
#         return False
    
# def isDecending(line):
#     try:
#         numbers = list(map(int, line.split()))
#         # Check if the list is sorted in decending order, also check if by at least one but not more than 3
#         return all(1 <= numbers[i] - numbers[i+1] <= 3 for i in range(len(numbers) - 1))
#     except ValueError:
#         return False
    
# def problemDamper(numbers):
#     # Try removing each number and check if the remaining sequence is ascending or descending
#     for i in range(len(numbers)):
#         modified = numbers[:i] + numbers[i+1:]
#         if isAscending(modified) or isDecending(modified):
#             return True
#     return False

# safeReports = 0
# with open('numbers.txt', 'r') as file:
#     for line in file:
#         if isAscending(line) or isDecending(line):
#             safeReports +=1
#         elif problemDamper(line):
#             safeReports +=1
#     print(safeReports)



def check(seq):
    return (
        all(0 < seq[i+1] - seq[i] <= 3 for i in range(len(seq)-1)) or
        all(-3 <= seq[i+1] - seq[i] < 0 for i in range(len(seq)-1)))

with open('numbers.txt') as file:
    sequences = [list(map(int, line.strip().split())) for line in file]

valid = sum(check(seq) for seq in sequences)

valid_with_problemDamper = sum( any(check(seq[:i] + seq[i+1:]) for i in range(len(seq)+1)) for seq in sequences)

print("Part 1:", valid)
print("Part 2:", valid_with_problemDamper)