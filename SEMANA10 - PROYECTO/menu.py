# menu.py
import actions # ← We import the file "actions.py" (it has all the functions to add/view/etc)
import data  # ← We import the file "data.py" (it has functions to save/load CSV)

# This function shows the MAIN MENU and handles user choices
def show_menu(): # ← FUNCTION starts here
    students = [] # ← We create an EMPTY LIST called "students" + This list will hold all student DICTIONARIES
    while True:                              # ← INFINITE LOOP – the menu repeats forever until we exit
        print("\nStudent Management System") # ← Prints a blank line + MENU title
        print("1. Add students")
        print("2. View all students")
        print("3. View top 3 students by average grade")
        print("4. View overall average grade")
        print("5. Export data to CSV")
        print("6. Import data from CSV")
        print("7. Exit") 
        
        choice = input("Enter your choice (1-7): ").strip() # ← Asks the user to type a number and removes extra spaces using ".strip()"
        
        # ──────────────────────────────
        #  CONDITIONS – What happens for each option - here we call functions from "actions.py" and "data.py"
        # ──────────────────────────────
        if choice == '1':  # ← User chose 1 → call the function that adds students
            actions.add_students(students) # ← CALLS function from actions.py - here the empty list "students" is passed as ARGUMENT to be modified as students are added
        elif choice == '2':
            actions.view_all_students(students) # ← CALLS function from actions.py to VIEW all students
        elif choice == '3':
            actions.view_top_3(students) # ← CALLS function from actions.py to VIEW top 3 students
        elif choice == '4':
            actions.view_overall_average(students) # ← CALLS function from actions.py to VIEW overall average
        elif choice == '5':
            data.export_to_csv(students) # ← CALLS function from data.py to EXPORT data to CSV
        elif choice == '6': # ← Loads students from a CSV file and REPLACES the current list
            students = data.import_from_csv(students) # ← CALLS function from data.py to IMPORT data from CSV and updates the "students" list
        elif choice == '7':
            print("Exiting the program.") # ← Exits the program
            break # ← BREAK = exit the infinite loop → program ends
        else: # ← This a safety net in case the user types something invalid (Worst case scenario)
            print("Invalid choice. Please enter a number between 1 and 7.") # ← If the user types anything else (0, 8, hello, etc.)