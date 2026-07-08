#create an empty list to store the numbers
numbers = []
#ask the user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

#print the list of numbers
print(f"The numbers entered were: {numbers}")

#get the highest number
highest = max(numbers)      
print(f"The highest number you entered is: {highest}")


