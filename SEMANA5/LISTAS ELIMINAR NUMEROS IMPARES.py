# Define my list of numbers
numbers = [42,23,25,70,27,29,31,96,33,74,35,98]

# iterate backwards through the list using a for loop
for i in range(len(numbers) - 1, -1, -1):
    # Check if the number is odd
    if numbers[i] % 2 != 0:
        # delete the odd number
        numbers.pop(i)

# print the list of even numbers
print(f"The list of even numbers is the following:{numbers}")