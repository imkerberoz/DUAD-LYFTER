import csv  # KEY TO HANDLE TAB-SEPARATED OR COMMA-SEPARATED FILES
import os   # TOOLBOX FOR WORKING WITH FILES ON YOUR COMPUTER

def enter_video_games():
    # ASK HOW MANY GAMES TO ADD (LIKE CHOOSING HOW MANY TOYS TO PUT IN A BOX)
    while True:
        try:
            n = int(input("How many video games do you want to enter? "))
            if n > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    # EMPTY LIST TO HOLD ALL OUR GAME INFO (LIKE AN EMPTY TOY BOX)
    video_games = []

    # COLLECT INFO FOR EACH GAME (FILLING THE TOY BOX ONE BY ONE)
    for i in range(n):
        print(f"\n--- Video Game {i+1} ---")
        
        name = input("Name: ").strip()
        while not name:
            name = input("Name can't be empty! Try again: ").strip()
        
        genre = input("Genre: ").strip()
        while not genre:
            genre = input("Genre can't be empty! Try again: ").strip()
        
        developer = input("Developer: ").strip()
        while not developer:
            developer = input("Developer can't be empty! Try again: ").strip()
        
        # CHECK FOR VALID ESRB RATING (LIKE MAKING SURE THE TOY HAS THE RIGHT AGE LABEL)
        valid_esrb = ["E", "E10+", "T", "M", "AO", "RP"]
        while True:
            rating = input("ESRB Rating (E, E10+, T, M, AO, RP): ").strip().upper()
            if rating in valid_esrb:
                break
            else:
                print("Oops! Pick one of: E, E10+, T, M, AO, RP")

        # ADD THIS GAME TO OUR LIST (PUT ONE TOY IN THE BOX)
        video_games.append({
            "Name": name,
            "Genre": genre,
            "Developer": developer,
            "ESRB Rating": rating
        })

    # SAVE TO A TAB-SEPARATED FILE (LIKE WRITING A NEAT LIST ON PAPER WITH TABS!)
    file_name = "video_games.tsv"  # .tsv means "Tab-Separated Values"
    
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Genre", "Developer", "ESRB Rating"], 
                                delimiter='\t')  # ← THIS IS THE MAGIC: '\t' = TAB!
        writer.writeheader()
        writer.writerows(video_games)
    
    print(f"\n Success! Your games are saved in '{file_name}' as a tab-separated file!")
    print(" Tip: Open it in Excel, Google Sheets, or any text editor — columns will line up perfectly!")

# RUN THE PROGRAM (LIKE PRESSING THE 'START' BUTTON)
if __name__ == "__main__":
    enter_video_games()