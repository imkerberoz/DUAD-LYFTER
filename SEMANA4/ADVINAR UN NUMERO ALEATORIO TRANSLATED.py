import random

# Generate a secret number between 1 and 10
secret_number = random.randint(1, 10)
print("Welcome, this is a game to guess a number between 1 and 10")
print("I wish you good luck")

while True:
    try:
        user_number = int(input("Enter a number between 1 and 10: "))
        if user_number == secret_number:
            print("Congratulations, you guessed the number")
            break   
        elif user_number < secret_number:
            print("The number is higher") 
        else:
            print("The number is lower")
    except ValueError:
        print("Please, enter a valid number")