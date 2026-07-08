
#INPUT WORDS FOR EXAMPLE USAGE
input_string = "Zinc-York-Walter-Born-Apple-Frank"

def sort_hyphenated_string(text):
    # SPLIT A LIST INTO A STRING BY HYPHEN (HERE WE ARE DISSECTING THE INPUT STRING)
    words = text.split('-')
    # SORT THE LIST ALPHABETICALLY  (THIS IS THE SECOND STEP/FILTER OF THE DISSECTION BASED ON THE GIVEN INSTRUCTIONS)
    words.sort()
    #JOIN THE LIST BACK INTO A STRING WITH HYPHENS (THIS IS THE THIRD FILTER)
    return '-'.join(words)

#FORMULATED RESULT
result = sort_hyphenated_string(input_string)
print(result)  