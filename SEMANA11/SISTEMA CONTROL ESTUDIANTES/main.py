#GRADE BOOK MANAGER COMMAND LINE INTERFACE
# main.py (THIS IS THE MAIN FILE THAT RUNS THE PROGRAM, THIS ONE DOESN'T CHANGE AT ALL, NO CHANGES ARE REQUIRED)

# We import the menu module to access the show_menu function - This is like the gates to the house
import menu  # ← We bring the file "menu.py" into this program - It contains the big menu with all the options

# ──────────────────────────────
#  FUNCTION: main() – This is the "starting point" of the program - It shows a WELCOME message and calls the menu
#  This is like the front door to the program with a welcome mat
# ──────────────────────────────
def main():  # ← FUNCTION starts here
    print("=== GradeBook CLI ===")  # ← Prints a fancy title
    print("Here you will control student grades efficiently.") # ← Friendly welcome message
    print("=" * 30) # ← Prints a line of 30 "=" signs, this is just for decoration/ aesthetics
    menu.show_menu() # ← CALLS the show_menu() function. IMPORTANT: this is where the actual program starts running

# ──────────────────────────────
#  THIS IS THE MOST IMPORTANT PART IN PYTHON PROGRAMS
# ──────────────────────────────
if __name__ == "__main__":  # ← This line checks if this file is being run directly (not imported as a module)
#     This line asks Python:
#    "Did the user double-click THIS file?"
#    If YES → run the code below
#    If someone imported this file → do nothing
    main()     # ← Actually starts the program! Without this line, nothing would happen