# student.py
# HERE WE CREATE A STUDENT CLASS TO REPRESENT EACH STUDENT AS AN OBJECT

class Student: #THIS IS THE CLASS DEFINITION, FOLLOWING THE ANALOGY OF REAL-WORLD OBJECTS, LIKE A FACTORY, A PATTERN, MOULD, ETC.
    def __init__(self, name, section, spanish, english, social, science): # THIS IS THE CONSTRUCTOR METHOD, IT INITIALIZES A NEW OBJECT WITH GIVEN ATTRIBUTES
        self.name = name # THESE ARE THE ATTRIBUTES OF THE STUDENT OBJECT (NAME, SECTION, GRADES)
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social = social
        self.science = science