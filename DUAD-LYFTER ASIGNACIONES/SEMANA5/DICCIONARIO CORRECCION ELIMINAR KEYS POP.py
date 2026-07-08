# FIRST DEFINE THE LIST OF KEYS TO BE REMOVED
list_of_keys = ['access_level', 'age']

# ORIGINAL DICTIONARY
employee = {
    'name': 'HILARY DUFF',
    'email': 'hilary@duff.com',
    'access_level': 5,
    'age': 32
}

# REMOVE EACH KEY THROUGH A LOOP USING pop() METHOD
for key in list_of_keys:
    employee.pop(key, None) 

# FINAL STEP IS TO PRINT THE DICTIONARY
print(employee)
