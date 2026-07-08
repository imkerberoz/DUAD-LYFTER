# Request data from the user
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

# Classify based on age
if age < 2:
    category = "Baby"  
elif 2 <= age < 10:
    category = "Child"  
elif 10 <= age < 13:
    category = "Pre-teen"   
elif 13 <= age < 18:   
    category = "Teenager"   
elif 18 <= age < 30:
    category = "Young Adult"
elif 30 <= age < 60:   
    category = "Adult"
else:
    category = "Senior"

# Display result
print(f"{name} {surname}, you are {age} years old and you are a {category}.")