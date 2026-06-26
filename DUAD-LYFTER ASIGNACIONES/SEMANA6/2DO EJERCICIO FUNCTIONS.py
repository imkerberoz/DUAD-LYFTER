#ATTEMPT TO ACCESS A VARIABLE DEFINED INSIDE A FUNCTION FROM THE OUTSIDE.

def create_local_variable():
    local_var = "I am local"  # THIS IS THE LOCAL VARIABLE DEFINED INSIDE THE FUNCTION
    print("Inside function:", local_var)

create_local_variable()

# TRY TO ACCESS local_var FROM OUTSIDE THE FUNCTION
print("Outside function:", local_var)




#TRY TO ACCESS A GLOBAL VARIABLE FROM INSIDE A FUNCTION AND CHANGE ITS VALUE.

global_var = "I am global"  # THIS IS A GLOBAL VARIABLE

def access_global_variable():
    global global_var # DECLARE THAT WE ARE USING THE GLOBAL VARIABLE, (global) IS USED AS A KEYWORD TO MODIFY THE GLOBAL VARIABLE INSIDE THE FUNCTION
    print("Inside function:", global_var)
    global_var = "I have been changed"  # CHANGE THE GLOBAL VARIABLE

access_global_variable()
print("Outside function:", global_var) # THIS WILL PRINT THE CHANGED VALUE, AND WILL NOT CAUSE AN ERROR BECAUSE WE USED THE 'global' KEYWORD.