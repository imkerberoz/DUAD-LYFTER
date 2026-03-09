# A SIMPLE DECORATOR THAT SHOWS FUNCTION CALL INFO IN A CLEAN WAY

def show_info(func): # DECORATOR DEFINITION, HERE func IS THE FUNCTION TO BE DECORATED
    def wrapper(*args, **kwargs): # THE WRAPPER FUNCTION THAT REPLACES THE ORIGINAL FUNCTION
        
        # PRINTS THE NAME OF THE FUNCTION BEING CALLED
        # USES func.__name__ TO GET THE ACTUAL NAME AS A STRING
        print(f"→ {func.__name__}()")
        
        # SHOWS POSITIONAL ARGUMENTS (args)
        # IF args IS EMPTY → SHOWS '(none)' USING THE 'or' TRICK
        # 'or' RETURNS THE FIRST TRUTHY VALUE → args IF NOT EMPTY, '(none)' IF EMPTY
        print(f"  Pos: {args or '(none)'}") #pos = POSITIONAL ARGUMENTS (ARGS)
        
        # SHOWS KEYWORD/NAMED ARGUMENTS (kwargs)
        # SAME 'or' TRICK: SHOWS DICT IF THERE ARE KWARGS, '(none)' IF EMPTY
        print(f"  Nom: {kwargs or '(none)'}") #nom = NAMED ARGUMENTS (KWARGS)
        
        # CALLS THE ORIGINAL FUNCTION WITH THE EXACT SAME ARGUMENTS
        # *args UNPACKS POSITIONAL ARGUMENTS
        # **kwargs UNPACKS KEYWORD ARGUMENTS
        # THIS IS THE MOST IMPORTANT LINE — THE REAL FUNCTION RUNS HERE
        result = func(*args, **kwargs)
        
        # PRINTS THE RETURN VALUE WITH A LEFT ARROW TO INDICATE RESULT
        print(f"← returns: {result}")
        
        # PRINTS A BEAUTIFUL LINE TO SEPARATE DIFFERENT FUNCTION CALLS
        # THIS IS JUST FOR AESTHETIC AND READABILITY PURPOSES
        # MAKES OUTPUT MUCH EASIER TO READ WHEN TESTING MULTIPLE CALLS
        print("✨" * 8)
        
        # VERY IMPORTANT: RETURNS THE ORIGINAL RESULT
        # SO THE DECORATED FUNCTION BEHAVES EXACTLY LIKE THE ORIGINAL ONE
        return result
    
    # THE DECORATOR MUST RETURN THE WRAPPER FUNCTION
    return wrapper


# ────────────────────────────────────────────────
# EXAMPLES OF USAGE
# ────────────────────────────────────────────────

@show_info #HERE WE APPLY THE DECORATOR TO THE add FUNCTION
def add(a, b): #HERE WE DEFINE A SIMPLE FUNCTION TO ADD TWO NUMBERS
    """Simple addition function"""
    return a + b #RETURNS THE SUM OF a AND b


@show_info #HERE WE APPLY THE DECORATOR TO THE greet FUNCTION
def greet(name, greeting="Hello", punctuation="!"):
    """Greets someone with customizable message"""
    return f"{greeting}, {name}{punctuation}" #RETURNS A FORMATTED GREETING STRING, TAKING INTO ACCOUNT OPTIONAL PARAMETERS


@show_info #HERE WE APPLY THE DECORATOR TO THE no_arguments FUNCTION
def no_arguments(): #THIS FUNCTION TAKES NO PARAMETERS, THIS IS TO SHOW THAT THE DECORATOR HANDLES IT GRACEFULLY
    """Function with zero parameters"""
    return "I'm running with no arguments!" #RETURNS A FIXED STRING


# ────────────────────────────────────────────────
# TEST CALLS
# ────────────────────────────────────────────────

print("Test 1 ───────────────") #THIS IS JUST A LABEL TO SEPARATE TESTS IN THE OUTPUT
add(10, 25)

print("Test 2 ───────────────")
greet("Sofia", greeting="Good morning", punctuation=" :)")

print("Test 3 ───────────────")
greet("Alex")

print("Test 4 ───────────────")
no_arguments()  # HERE WE CALL THE FUNCTION WITH NO ARGUMENTS, TO PROVE THE DECORATOR HANDLES FUNCTIONS WITHOUT PARAMETERS
                # THIS IS USEFUL TO SHOW THE VERSATILITY OF THE DECORATOR
                # THIS IS THANKS TO THE USE OF *args AND **kwargs IN THE WRAPPER FUNCTION INSIDE THE DECORATOR