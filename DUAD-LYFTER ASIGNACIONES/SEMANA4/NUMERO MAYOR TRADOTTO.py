try:
    # Ask the user for three numbers
    num1 = float(input("Enter the first number: "))   
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Compare the numbers to find the largest
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    # Display the result (largest number)
    print("The largest number is:", largest)
except ValueError:
    print("Please, ensure you enter only valid numbers.")