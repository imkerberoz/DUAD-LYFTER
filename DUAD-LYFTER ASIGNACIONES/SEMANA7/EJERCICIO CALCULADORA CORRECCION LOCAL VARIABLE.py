# CALCULATOR WITH LOCAL VARIABLES - NO GLOBAL VARIABLES

# FUNCTION DEFINITIONS (all receive and return local values)
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b    

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def reset_calculator():
    return 0.0

"""MAIN FUNCTION - encapsulates the entire program logic to avoid global variables"""
def main():
    current_number = 0.0  #THIS IS THE LOCAL VARIABLE TO TRACK THE CURRENT NUMBER (CORRECION FROM GLOBAL VARIABLE)

    while True:
        # DISPLAY MENU
        print("\nCalculator - Current number:", current_number) #THIS IS RANGE 1
        print("1. Addition")                                    #THIS IS RANGE 2
        print("2. Subtraction")                                 #THIS IS RANGE 3
        print("3. Multiplication")                              #THIS IS RANGE 4
        print("4. Division")                                    #THIS IS RANGE 5
        print("5. Reset result")                                #THIS IS RANGE 6
        print("6. Exit")                                        #THIS IS RANGE 7

        # GET OPERATION, HERE WE ARE ASKING THE USER TO SELECT AN OPTION AND HANDLING INVALID INPUTS (THIS IS PART OF THE MAIN LOOP)
        try:   
            operation = int(input("Select an option (1-6): "))
            if operation not in range(1, 7): #HERE WE ARE COVERING THE CASE WHERE THE USER ENTERS A NUMBER OUTSIDE THE VALID RANGE
                print("Error: Invalid option. Please select an option between 1 and 6.")
                continue
        except ValueError: #HERE WE ARE COVERING THE CASE WHERE THE USER ENTERS A NON-NUMERIC VALUE
            print("Error: Please enter a valid number for the option.")
            continue

        #SECOND PART SECOND PART SECOND PART SECOND PART SECOND PART  SECOND PART SECOND PART SECOND PART SECOND PART
        # HANDLE EXIT
        if operation == 6:
            print("Thank you for using the calculator!")
            break

        # HANDLE RESET
        if operation == 5:
            current_number = reset_calculator()
            print(f"The calculator has been reset. Current number: {current_number}")
            continue

        # GET NEW NUMBER
        try:
            new_number = float(input("Enter a number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

            #THIRD AND FINAL PART THIRD AND FINAL PART THIRD AND FINAL PART THIRD AND FINAL PART THIRD AND FINAL PART THIRD AND FINAL PART
                # PERFORM OPERATION, HERE WE ARE CALLING THE APPROPRIATE FUNCTION BASED ON USER SELECTION (OPERATION + RESULT DISPLAY)
        if operation == 1:
            current_number = addition(current_number, new_number)
            print(f"Result: {current_number}")
        elif operation == 2:
            current_number = subtraction(current_number, new_number)
            print(f"Result: {current_number}")
        elif operation == 3:
            current_number = multiplication(current_number, new_number)
            print(f"Result: {current_number}")
        elif operation == 4:
            result = division(current_number, new_number)
            if isinstance(result, str):
                print(result)
            else:
                current_number = result
                print(f"Result: {current_number}")

# CALL MAIN FUNCTION TO START THE PROGRAM
if __name__ == "__main__":
    main()