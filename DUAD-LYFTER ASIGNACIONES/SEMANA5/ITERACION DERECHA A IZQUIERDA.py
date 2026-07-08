# Define the string
my_string = 'I am hungry'

# Check if the string is empty
if not my_string:
    print("The string is empty.")
else:
    # Iterate from right to left using range
    for i in range(len(my_string) - 1, -1, -1):
        print(my_string[i])