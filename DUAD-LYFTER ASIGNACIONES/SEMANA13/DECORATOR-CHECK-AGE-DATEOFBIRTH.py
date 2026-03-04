# THE User CLASS HAS A PROPERTY age THAT CALCULATES THE AGE BASED ON THE CURRENT DATE AND THE date_of_birth ATTRIBUTE
# THE DECORATOR REQUIRES ADULT AGE (18 OR OLDER) TO ALLOW THE FUNCTION TO EXECUTE, OTHERWISE IT RAISES A ValueError WITH A CLEAR MESSAGE
# THIS IS A PRACTICAL EXAMPLE OF HOW DECORATORS CAN BE USED FOR VALIDATION AND ACCESS CONTROL IN REAL-WORLD SCENARIOS, SUCH AS CHECKING LEGAL AGE FOR CERTAIN ACTIONS

from datetime import datetime  # WE IMPORT datetime TO WORK WITH DATES AND CALCULATE AGE ACCURATELY

# ______________________________________________________________________________________________
""" 1. WE CREATE A VERY BASIC USER CLASS """
class User:
    def __init__(self, name, date_of_birth): #THIS IS THE CONSTRUCTOR METHOD THAT INITIALIZES THE USER OBJECT WITH A NAME AND A DATE OF BIRTH
        self.name = name  # STORE THE USER'S NAME
        self.date_of_birth = date_of_birth # STORE DATE OF BIRTH (MUST BE A datetime.date OBJECT)


# ______________________________________________________________________________________________
    """ 2. WE CREATE A PROPERTY THAT CALCULATES AGE AUTOMATICALLY EVERY TIME IT IS ACCESSED """
    # THIS PROPERTY USES THE CURRENT DATE AND date_of_birth TO CALCULATE AGE IN YEARS
    # IT CORRECTLY HANDLES CASES WHERE THE BIRTHDAY HAS NOT YET OCCURRED THIS YEAR
    # THIS IS WHAT THEY REQUESTED ON THE EXERCISE: A PROPERTY THAT CALCULATES AGE BASED ON DATE OF BIRTH, AND CAN BE USED IN THE DECORATOR TO CHECK IF THE USER IS AN ADULT
    # PROPERTIES ARE ACCESSED LIKE NORMAL ATTRIBUTES (NO PARENTHESES NEEDED)
    # IMPORTANT: THIS IS A READ-ONLY PROPERTY (GETTER) — WE ARE NOT CREATING A SETTER HERE
    
    @property  # THE @property DECORATOR LETS US DEFINE A METHOD THAT BEHAVES LIKE AN ATTRIBUTE
    def age(self):
        today = datetime.now().date()  # GET TODAY'S DATE (ONLY THE DATE PART — NO TIME) - THE LAST PART .date() CONVERTS THE datetime OBJECT TO A date **ONLY** OBJECT, WHICH IS NECESSARY FOR THE CALCULATION
        birth_date = self.date_of_birth  # SHORT NAME FOR THE STORED BIRTH DATE - THE SELF.DATE_OF_BIRTH ATTRIBUTE HOLDS THE USER'S BIRTH DATE AS A datetime.date OBJECT
        calculated_age = today.year - birth_date.year # BASIC AGE CALCULATION BASED ON YEAR DIFFERENCE
        
        # VERY IMPORTANT: IF THE BIRTHDAY HAS NOT HAPPENED YET THIS YEAR = SUBTRACT 1
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            calculated_age -= 1
            
        return calculated_age # RETURN THE FINAL CALCULATED AGE


# ______________________________________________________________________________________________
""" 3. WE CREATE A DECORATOR THAT CHECKS IF THE USER IS OF LEGAL AGE (18+)"""
def require_adult(func): # THE func PARAMETER REPRESENTS THE FUNCTION THAT WE WANT TO DECORATE (THE ONE THAT REQUIRES ADULT CHECK)
    def wrapper(user, *args, **kwargs): # THE WRAPPER FUNCTION REPLACES THE ORIGINAL FUNCTION
        if user.age < 18: # CHECK IF THE USER IS UNDER 18 YEARS OLD
            raise ValueError(f"{user.name} is underage (age {user.age})") # RAISE A CLEAR EXCEPTION INCLUDING THE USER'S NAME AND ACTUAL AGE
        return func(user, *args, **kwargs) # IF THE CHECK PASSES, CALL THE ORIGINAL FUNCTION WITH ALL ARGUMENTS INTACT (INCLUDING THE USER OBJECT)
    
    return wrapper # THE DECORATOR RETURNS THIS WRAPPER FUNCTION


"""────────────────────────────────────────── EXAMPLE USAGE ────────────────────────────────────────"""
# NOW WE PUT EVERYTHING TOGETHER WITH SOME EXAMPLE USERS AND A FUNCTION THAT REQUIRES ADULT CHECK

# WE CREATE TWO USERS WITH DIFFERENT BIRTH DATES TO TEST THE DECORATOR
joshua = User("Joshua", datetime(2005, 6, 15).date())    # ≈ 20 YEARS OLD (depending on current year)
gilfer = User("Gilfer", datetime(2010, 3, 22).date())  # ≈ 17 YEARS OLD (depending on current year)


# EXAMPLE FUNCTION THAT ONLY ADULTS SHOULD BE ALLOWED TO USE
@require_adult # APPLY THE DECORATOR TO THIS FUNCTION TO ENFORCE THE ADULT CHECK
def buy_alcohol(user): # THIS FUNCTION SIMULATES THE ACTION OF BUYING ALCOHOL, WHICH SHOULD ONLY BE ALLOWED FOR USERS WHO ARE 18 OR OLDER
    print(f"{user.name} ({user.age} years old) can buy alcohol!") # THIS LINE ONLY EXECUTES IF THE DECORATOR ALLOWS IT


# ── TESTS ────────────────────────────────────────

# DISPLAY AGES
print(f"{joshua.name} is {joshua.age} years old")
print(f"{gilfer.name} is {gilfer.age} years old")
print()

# THIS CALL SHOULD SUCCEED
buy_alcohol(joshua)

# THIS CALL SHOULD FAIL AND SHOW THE ERROR MESSAGE
try:
    buy_alcohol(gilfer)
except ValueError as errordetails:
    print("Error:", errordetails)