# actions.py
import student  # ← Importamos la clase Student desde student.py

# ──────────────────────────────
#  FUNCTION #1: add_students(students)
#  Purpose: WE WILL ASK THE USER TO ADD MULTIPLE STUDENTS AND THEIR GRADES (THIS USED TO MODIFY A LIST OF DICTIONARIES, NOW MODIFIES A LIST OF OBJECTS)
# ──────────────────────────────
def add_students(students):  # STUDENTS IS A LIST THAT WILL HOLD OBJECTS OF TYPE Student
    try:
        n = int(input("Enter the number of students to add: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    for _ in range(n):
        name = input("Enter full name: ").strip()
        section = input("Enter section (e.g., 11B): ").strip()
        
        spanish = get_valid_grade("Spanish")
        english = get_valid_grade("English")
        social = get_valid_grade("Social Studies")
        science = get_valid_grade("Sciences")
        
        # HERE IS WHERE THE MAGIC HAPPENS, WE CREATE A STUDENT OBJECT AND ADD IT TO THE LIST (LIKE BEFORE WE ADDED A DICTIONARY, BUT NOW WE ADD AN OBJECT)
        new_student = student.Student(name, section, spanish, english, social, science)
        students.append(new_student)
        print("Student added successfully.")

# ──────────────────────────────
#  FUNCTION #2: GET VALID GRADE INPUT FROM USER, THIS IS A HELPER FUNCTION TO AVOID INVALID GRADES
#  (THIS FUNCTION REMAINS THE SAME AS BEFORE, HERE WE JUST VALIDATE THAT THE GRADE IS A NUMBER BETWEEN 0 AND 100)
# ──────────────────────────────
def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# ──────────────────────────────
#  FUNCTION #3: view_all_students(students)
#  Purpose: THIS ONE DISPLAYS ALL STUDENTS AND THEIR GRADES (MODIFIED TO WORK WITH OBJECTS INSTEAD OF DICTIONARIES)
# ──────────────────────────────
def view_all_students(students):
    if not students:
        print("No students added yet.")
        return
    
    for student in students:  # student IS AN OBJECT OF TYPE Student FROM student.py
        print(f"Name: {student.name}")
        print(f"Section: {student.section}")
        print(f"Spanish: {student.spanish}")
        print(f"English: {student.english}")
        print(f"Social Studies: {student.social}")
        print(f"Sciences: {student.science}")
        print("---")

# ──────────────────────────────
#  FUNCTION #4: CALCULATE AVERAGE GRADE FOR A STUDENT (student OBJECT)
#  Purpose: CALCULATE THE AVERAGE OF THE 4 SUBJECTS FOR A GIVEN STUDENT OBJECT
# ──────────────────────────────
def calculate_average(student):  # student IS AN OBJECT OF TYPE Student
    return (student.spanish + student.english + student.social + student.science) / 4

# ──────────────────────────────
#  FUNCTION #5: view_top_3(students)
#  Purpose: SHOWS THE TOP 3 STUDENTS BASED ON AVERAGE GRADE
# ──────────────────────────────
def view_top_3(students):
    if not students:
        print("No students added yet.")
        return
    
    # SORT STUDENTS BY AVERAGE GRADE IN DESCENDING ORDER
    sorted_students = sorted(students, key=calculate_average, reverse=True)
    top_3 = sorted_students[:3]
    
    print("Top 3 students by average grade:")
    for i, student in enumerate(top_3, 1):
        avg = calculate_average(student)
        print(f"{i}. {student.name} ({student.section}) - Average: {avg:.2f}")

# ──────────────────────────────
#  FUNCTION #6: VIEW OVERALL AVERAGE GRADE OF ALL STUDENTS
#  Purpose: CALCULATE AND DISPLAY THE OVERALL AVERAGE GRADE ACROSS ALL STUDENTS
# ──────────────────────────────
def view_overall_average(students):
    if not students:
        print("No students added yet.")
        return
    
    total_avg = sum(calculate_average(s) for s in students) / len(students)
    print(f"Overall average grade: {total_avg:.2f}")