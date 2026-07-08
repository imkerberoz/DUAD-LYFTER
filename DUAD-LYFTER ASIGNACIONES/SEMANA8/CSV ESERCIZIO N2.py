import csv #THIS IS LIKE A KEY TO OPEN A SPECIAL DOOR FOR HANDLING CSV FILES
import os  #THIS IS LIKE A TOOLBOX FOR HANDLING FILES AND DIRECTORIES WITHIN THE OPERATING SYSTEM (OUR COMPUTER)

def enter_video_games():
    # HERE WE ARE ASKING THE USER HOW MANY VIDEO GAMES THEY WANT TO ENTER (IT'S LIKE ASKING HOW MANY ITEMS TO ADD TO A SHOPPING CART)
    while True:
        try:
            n = int(input("How many video games do you want to enter? "))
            if n > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    # HERE WE ARE CREATING AN EMPTY LIST TO STORE VIDEO GAME DATA (ITS LIKE AN EMPTY SHOPPING CART)
    video_games = []

    # HERE WE ARE COLLECTING DATA FOR EACH VIDEO GAME (IT'S LIKE ADDING ITEMS TO THE SHOPPING CART)
    for i in range(n):
        print(f"\n--- Video Game {i+1} ---")
        
        name = input("Name: ").strip()
        while not name:
            name = input("The name cannot be empty. Enter the name: ").strip()
        
        genre = input("Genre: ").strip()
        while not genre:
            genre = input("The genre cannot be empty. Enter the genre: ").strip()
        
        developer = input("Developer: ").strip()
        while not developer:
            developer = input("The developer cannot be empty. Enter the developer: ").strip()
        
        # BASIC VALIDATION FOR ESRB RATING (WE GO THROUGH A LOOP UNTIL A VALID RATING IS ENTERED)
        valid_esrb = ["E", "E10+", "T", "M", "AO", "RP"]
        while True:
            rating = input("ESRB Rating (E, E10+, T, M, AO, RP): ").strip().upper()
            if rating in valid_esrb:
                break
            else:
                print("Invalid rating. Options are: E, E10+, T, M, AO, RP")

        # DICTIONARY TO STORE VIDEO GAME DATA (IT'S LIKE A SMALL BOX FOR EACH ITEM)
        video_games.append({
            "Name": name,
            "Genre": genre,
            "Developer": developer,
            "ESRB Rating": rating
        })

    # HERE WE ARE WRITING THE DATA TO A CSV FILE (IT'S LIKE CHECKING OUT THE SHOPPING CART)
    file_name = "video_games.csv"
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Genre", "Developer", "ESRB Rating"])
        writer.writeheader()
        writer.writerows(video_games)
    
    print(f"\nData successfully saved to '{file_name}'!") # CONFIRMATION MESSAGE (IT'S LIKE A RECEIPT AFTER CHECKOUT)
    

# HERE WE CALL THE MAIN FUNCTION TO RUN THE PROGRAM
if __name__ == "__main__":
    enter_video_games()