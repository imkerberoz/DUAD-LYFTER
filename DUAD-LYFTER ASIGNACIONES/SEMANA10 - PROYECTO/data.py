# data.py 
# +++++++++++++++++++ data.py – Save and Load students from CSV file +++++++++++++++++++


import csv   # ← Python's magic tool to work with CSV files (like Excel)
import os    # ← Tool to check if a file exists on the computer

# ──────────────────────────────
#  GLOBAL VARIABLE – Name of the CSV file
# ──────────────────────────────
CSV_FILE = 'students.csv'         # ← All students will be saved in this file / It's like a spreadsheet on one's computer


# ──────────────────────────────
#  FUNCTION #1: export_to_csv(students)
#  Purpose: Saves the entire LIST of students to a CSV file
# ──────────────────────────────
def export_to_csv(students):   # ← FUNCTION starts, receives the big LIST of student DICTIONARIES
    if not students:                     # ← This is in case the list is empty, so we don't create an empty file
        print("No data to export.")
        return                           # ← The program STOPS – nothing to save
    
    # ── Open the file to WRITE ('w') a new CSV ──
    with open(CSV_FILE, 'w', newline='') as file:     # ← 'w' = write mode (creates file if missing), the newline='' avoids blank lines on WINDOWS
        writer = csv.DictWriter(file, fieldnames=['name', 'section', 'spanish', 'english', 'social', 'science']) # Tell CSV which columns (keys) we want + +  DictWriter = writes DICTIONARIES directly to CSV
        writer.writeheader()                 # ← Writes the header row with column NAMES, like "name", "section", etc.
        writer.writerows(students)          # ← Writes ALL student dictionaries at once!
    
    print(f"Data exported to {CSV_FILE}.")   # ← Success message – now you can open it in Excel!



# ──────────────────────────────
#  FUNCTION #2: import_from_csv(current_students)
#  Purpose: Load students from the CSV file and return them as a LIST
# ──────────────────────────────
def import_from_csv(current_students):   # ← FUNCTION starts, receives the current LIST of students (could be empty)
    if not os.path.exists(CSV_FILE):                # ← Check: does the file exist on our computer?
        print("No previously exported file found.")    # ← Return the old list (nothing changed)
        return current_students
    
    
    with open(CSV_FILE, 'r') as file:         # ← Open the file to READ ('r')  ['r' = read mode]
        reader = csv.DictReader(file)        # ← Reads the CSV into DICTIONARIES automatically
        imported_students = list(reader)     # ← Convert the reader object to a LIST of DICTIONARIES [Now imported_students looks exactly like our normal list!]
    
    # Convert grades back to float  -- Fixes the grades: CSV saves them as text → we need numbers again ──  We must do this because math (averages) only works with numbers!
    for student in imported_students:                     # ← Loop through each loaded student
        student['spanish'] = float(student['spanish'])    # ← Convert each grade from text to float number -- Convert text "95.5" → real number 95.5
        student['english'] = float(student['english'])
        student['social'] = float(student['social'])
        student['science'] = float(student['science'])
    
    print(f"Data imported from {CSV_FILE}. {len(imported_students)} students loaded.")  # ← Success message with number of loaded students
    return imported_students   # ← Return the new list of students loaded from the CSV