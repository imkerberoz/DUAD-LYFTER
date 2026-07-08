#CREATE A FUNCTION THAT HELP TURN A WORD AROUND AND RETURN IT
def reverse_word(word):
    return word[::-1]   
#TEST THE FUNCTION
print(reverse_word("Hello"))  # Output: "olleH"


#THIS IS ANOTHER EXAMPLE OF A FUNCTION BUT THIS ONE DOESN'T RETURN ANYTHING, IT JUST PRINTS (SHOWS) THE REVERSED WORD TO THE USER
def reverse_and_print(word):
    reversed_word = word[::-1]
    print(reversed_word)    

reverse_and_print("GOODBYE")  # Output: "EYBDOG"