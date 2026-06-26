from datetime import date


# MINIMAL USER CLASS
class User:
    def __init__(self, date_of_birth):
        # STORE BIRTH DATE (MUST BE A date OBJECT)
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        # GET CURRENT DATE
        today = date.today()
        
        # CALCULATE AGE IN YEARS
        age = today.year - self.date_of_birth.year
        
        # CORRECT AGE IF BIRTHDAY HAS NOT HAPPENED YET THIS YEAR
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
            
        # RETURN THE AGE
        return age


# VERY SIMPLE DECORATOR TO REQUIRE AGE 18+
def must_be_adult(func):
    def wrapper(user):
        # CHECK IF USER IS UNDER 18
        if user.age < 18:
            # RAISE EXCEPTION IF TOO YOUNG
            raise ValueError("Must be 18 or older")
        
        # IF OK → RUN THE ORIGINAL FUNCTION
        return func(user)
    
    # RETURN THE WRAPPER FUNCTION
    return wrapper


# EXAMPLE FUNCTION THAT ONLY ADULTS CAN USE
@must_be_adult
def buy_alcohol(user):
    # THIS ONLY RUNS IF THE DECORATOR ALLOWS IT
    print(f"{user.age}-year-old adult can buy alcohol")


# ── SMALL USAGE EXAMPLE ───────────────────────────────────────────────

# CREATE TWO USERS (assuming current date is around Feb 2026)
adult   = User(date(2005, 7, 10))     # ≈ 20 years old
teen    = User(date(2009, 4, 20))     # ≈ 16–17 years old

# TEST THE FUNCTION
print("Adult age:", adult.age)        # should print ~20
print("Teen age: ", teen.age)         # should print ~16 or 17

try:
    buy_alcohol(adult)                # THIS SHOULD WORK
    buy_alcohol(teen)                 # THIS SHOULD RAISE EXCEPTION
except ValueError as e:
    print("Error caught:", e)