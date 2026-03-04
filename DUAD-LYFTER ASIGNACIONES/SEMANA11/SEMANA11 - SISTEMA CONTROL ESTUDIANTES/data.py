# data.py
import csv
import os
import student  # THIS IS A NEW ADDITION - WE IMPORT THE student MODULE TO CREATE Student OBJECTS

CSV_FILE = 'students.csv'

# ──────────────────────────────
#  FUNCTION #1: EXPORT TO CSV(students)
#  Purpose: SAVES THE LIST OF Student OBJECTS TO A CSV FILE
# ──────────────────────────────
def export_to_csv(students):
    if not students:
        print("No data to export.")
        return
    
    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'section', 'spanish', 'english', 'social', 'science'])
        writer.writeheader()
        
        # WE CONVERT EACH Student OBJECT TO A DICTIONARY BEFORE WRITING TO CSV (THIS IS TEMPORARY FOR CSV STORAGE)
        for student in students:
            student_dict = {
                'name': student.name,
                'section': student.section,
                'spanish': student.spanish,
                'english': student.english,
                'social': student.social,
                'science': student.science
            }
            writer.writerow(student_dict)
    
    print(f"Data exported to {CSV_FILE}.") # CONFIRMATION MESSAGE

# ──────────────────────────────
#  FUNCTION #2: import_from_csv(current_students)
#  Purpose: WE LOAD STUDENT DATA FROM A CSV FILE AND RETURN A LIST OF Student OBJECTS
# ──────────────────────────────
def import_from_csv(current_students):
    if not os.path.exists(CSV_FILE):
        print("No previously exported file found.")
        return current_students
    
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        imported_data = list(reader)
    
    # WE CONVERT EACH DICTIONARY FROM CSV BACK INTO A Student OBJECT, HERE IS THE MAGIC HAPPENING
    imported_students = []
    for data in imported_data:
        student_obj = student.Student(
            data['name'],
            data['section'],
            float(data['spanish']),
            float(data['english']),
            float(data['social']),
            float(data['science'])
        )
        imported_students.append(student_obj)
    
    print(f"Data imported from {CSV_FILE}. {len(imported_students)} students loaded.")
    return imported_students