# ASK FOR THE NUMBER OF GRADES FROM THE STUDENT
try:
    total_grades = int(input("Enter the number of grades you want to average: "))
    if total_grades <= 0:
        print("Error: The number of grades must be a positive number.")
        exit()

    # INITIALIZE VARIABLES
    count_passing_grades = 0
    count_failing_grades = 0 
    sum_passing_grades = 0
    sum_failing_grades = 0
    total_sum_grades = 0

    # LOOP TO READ EACH GRADE
    for grade_counter in range(1, total_grades + 1):
        try:
            current_grade = float(input(f"Enter grade number {grade_counter}: "))
            # VALIDATE THAT THE GRADE IS BETWEEN 0 AND 100
            if current_grade < 0 or current_grade > 100:
                print("Error: The grade must be between 0 and 100.")
                exit()
            
            if current_grade < 70:
                # FAILING GRADE
                count_failing_grades += 1
                sum_failing_grades += current_grade
            else:
                # PASSING GRADE
                count_passing_grades += 1
                sum_passing_grades += current_grade
            
            # TOTAL SUM OF GRADES (OVERALL AVERAGE)
            total_sum_grades += current_grade
        except ValueError:
            print("Error: Invalid input. Please enter a valid grade.")
            exit()

    # CALCULATE AVERAGES
    overall_average = total_sum_grades / total_grades if total_grades > 0 else 0
    passing_average = sum_passing_grades / count_passing_grades if count_passing_grades > 0 else 0
    failing_average = sum_failing_grades / count_failing_grades if count_failing_grades > 0 else 0

    # DISPLAY RESULTS
    print("\n--RESULTS--\n")
    print(f"Number of passing grades: {count_passing_grades}")
    print(f"Average of passing grades: {passing_average:.2f}")
    print(f"Number of failing grades: {count_failing_grades}")
    print(f"Average of failing grades: {failing_average:.2f}")
    print(f"Overall average of grades: {overall_average:.2f}")
    
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
    exit()