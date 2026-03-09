#CREATE A FUNCTION THAT PRINTS THE NUMBER OF UPPERCASE AND LOWERCASE LETTERS IN A STRING.

def count_case_letters(input_string): #HERE WE DEFINE THE FUNCTION NAME
    upper_count = 0 #COUNTER FOR UPPER CASE LETTERS (ALWAYS INITIALIZED TO 0)
    lower_count = 0 #COUNTER FOR LOWER CASE LETTERS (ALWAYS INITIALIZED TO 0)
    
    for char in input_string: #HERE WE LOOP THROUGH EACH CHARACTER IN THE STRING
        if char.isupper(): # FORMULA = IF CHARACTER IS UPPER CASE
            upper_count += 1 #IF THE CHARACTER IS UPPER CASE, WE INCREMENT THE UPPER CASE COUNTER BY 1 (+= 1)
        elif char.islower(): # FORMULA = IF CHARACTER IS LOWER CASE
            lower_count += 1 #IF THE CHARACTER IS LOWER CASE, WE INCREMENT THE LOWER CASE COUNTER BY 1 (+=1)
            
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")

#HERE WE DEFINE THE STRING TO BE ANALYZED
count_case_letters("I am tRyInG mY reaLly beST")

