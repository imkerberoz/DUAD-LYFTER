# actions.py

# ──────────────────────────────
#  FUNCTION #1: add_students(students)
#  Purpose: Ask the user how many students to add, then add them one by one
# ──────────────────────────────
def add_students(students): # ← FUNCTION starts here AND takes "students" list as ARGUMENT
    try: # ← We use TRY-EXCEPT to handle invalid input
        n = int(input("Enter the number of students to add: ")) # ← Ask how many students to add
    except ValueError: # ← If the user types something invalid (like "five" instead of 5)
        print("Invalid input. Please enter a number.") 
        return # ← STOPS the function immediately due to invalid input
    
    for _ in range(n): # ← Loop n times to add each student - That's to say, Repeat n times (the _ means "I don't use the counter"), 
        student = {} # ← Create an EMPTY DICTIONARY to hold the student's data
        student['name'] = input("Enter full name: ").strip()  # ← Get the student's name and remove extra spaces using ".strip()"
        student['section'] = input("Enter section (e.g., 11B): ").strip() # ← Get the section and remove extra spaces using ".strip()"
        
# ── Ask grades using the helper function below ──
        student['spanish'] = get_valid_grade("Spanish") # ← Get valid grade for Spanish
        student['english'] = get_valid_grade("English")
        student['social'] = get_valid_grade("Social Studies")
        student['science'] = get_valid_grade("Sciences")
        
        students.append(student) # ← Add this new DICTIONARY to the big LIST "students"
        print("Student added successfully.") # ← Confirmation message


# ──────────────────────────────
#  FUNCTION #2: get_valid_grade(subject)
#  Purpose: Keep asking for a grade until it's a valid number between 0 and 100
# ──────────────────────────────
def get_valid_grade(subject): # ← FUNCTION starts here and takes "subject" as ARGUMENT
    while True: # ← INFINITE LOOP – keeps asking until a valid grade is entered
        try: # ← We use TRY-EXCEPT to handle invalid input
            grade = float(input(f"Enter grade for {subject} (0-100): ")) # ← Ask for the grade and convert it to float
            if 0 <= grade <= 100: # ← Check if the grade is between 0 and 100
                return grade # ← SUCCESS → give the grade back and exit
            else: #This is a safety net in case the user types a number outside the valid range
                print("Grade must be between 0 and 100.")
        except ValueError: 
            print("Invalid input. Please enter a number.") # ← If the user types something invalid (like "A" instead of 85)


# ──────────────────────────────
#  FUNCTION #3: view_all_students(students)
#  Purpose: Show every student and all their grades
# ──────────────────────────────
def view_all_students(students): # ← FUNCTION starts here AND takes "students" list as ARGUMENT
    if not students:                    # ← Check if the list is empty and if so, print a message and return
        print("No students added yet.") 
        return                                 # ← Stop here if there are no students
    
    for student in students:                  # ← Loop through each DICTIONARY in the LIST
        print(f"Name: {student['name']}")
        print(f"Section: {student['section']}")
        print(f"Spanish: {student['spanish']}")
        print(f"English: {student['english']}")
        print(f"Social Studies: {student['social']}")
        print(f"Sciences: {student['science']}")
        print("---")                              # ← Print a separator between students - This is for better readability



# ──────────────────────────────
#  FUNCTION #4: calculate_average(student)
#  Purpose: Calculate the average of one student's 4 grades
# ──────────────────────────────
def calculate_average(student): # ← FUNCTION starts here AND takes ONE "student" DICTIONARY as ARGUMENT
    return (student['spanish'] + student['english'] + student['social'] + student['science']) / 4  # ← Adds the 4 grades and divides by 4


# ──────────────────────────────
#  FUNCTION #5: view_top_3(students)
#  Purpose: Show the 3 students with the highest average
# ──────────────────────────────
def view_top_3(students):  # ← FUNCTION starts here AND takes "students" list as ARGUMENT
    if not students:                   # ← Check if the list is empty and if so, print a message and return
        print("No students added yet.")
        return
    
    # ← Sort the list by average (highest first)
    sorted_students = sorted(students, key=calculate_average, reverse=True)
    #     sorted()     → creates a new sorted list
    #     key=         → tells Python to sort using the result of calculate_average
    #     reverse=True → from highest to lowest
    top_3 = sorted_students[:3]   # ← Takes only the first 3 students from the sorted list

    
    
    print("Top 3 students by average grade:")
    for i, student in enumerate(top_3, 1):     # ← enumerate gives 1,2,3 instead of 0,1,2
        avg = calculate_average(student)
        print(f"{i}. {student['name']} ({student['section']}) - Average: {avg:.2f}") #     :.2f → shows only 2 decimal places


# ──────────────────────────────
#  FUNCTION #6: view_overall_average(students)
#  Purpose: Calculate and show the average of ALL students together
# ──────────────────────────────
def view_overall_average(students): # ← FUNCTION starts here AND takes "students" list as ARGUMENT
    if not students:
        print("No students added yet.")
        return
    
    total_avg = sum(calculate_average(s) for s in students) / len(students)  # ← Calculate average of all students' averages
    #     sum(...) → adds all averages
    #     len(students) → how many students there are
    print(f"Overall average grade: {total_avg:.2f}")  # ← Shows the overall average with 2 decimal places