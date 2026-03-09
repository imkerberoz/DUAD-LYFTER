class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    # THIS CLASS REPRESENTS A PERSON WITH A NAME ATTRIBUTE AND A STRING REPRESENTATION 
    # THIS WILL BE USEFUL TO IDENTIFY PASSENGERS ON THE BUS AND PRINT THEIR NAMES


# FOLLOWING THE ANALOGY OF A FACTORY, HERE WE ARE CREATING THE FACTORY/CLASS FOR A BUS
# THIS HELPS US MANAGE PASSENGERS AND CAPACITY AND ALSO HELPS CREATE RULES ABOUT BOARDING AND ALIGHTING
class Bus:
    def __init__(self, max_passengers): # CONSTRUCTOR THAT TAKES MAXIMUM PASSENGERS AS A PARAMETER/VARIABLE
        self.max_passengers = max_passengers    # MAXIMUM CAPACITY OF THE BUS (FIXED VALUE)
        self.passengers = []                    # EMPTY LIST TO HOLD CURRENT PASSENGERS
        print(f"This bus has a maximum capacity of {max_passengers} people.") # THIS IS A FRIENDLY MESSAGE TO INDICATE THE BUS CAPACITY

    def add_passenger(self, person): # THIS METHOD ADDS A PASSENGER TO THE BUS
        """THIS METHOD BOARDS A PASSENGER ON THE BUS, ONLY IF THERE IS SPACE"""
        if len(self.passengers) < self.max_passengers: # CHECK IF THERE IS SPACE ON THE BUS (HERE WE TAKE THE CURRENT NUMBER OF PASSENGERS (EMPTY LIST OF PASSENGERS CREATED ABOVE) AND COMPARE IT TO THE MAXIMUM CAPACITY (ALSO MENTIONED ABOVE))
            self.passengers.append(person) #AT THIS POINT WE ADD THE PERSON TO THE LIST OF PASSENGERS BECAUSE WE HAVE CONFIRMED THAT THERE'S ENOUGH SPACE
            print(f"{person} has boarded the bus.") # FRIENDLY MESSAGE TO CONFIRM THE PERSON HAS BOARDED
        else:
            print("The bus is full. No more passengers can board.") # FRIENDLY MESSAGE TO INDICATE THE BUS IS FULL

    def remove_passenger(self, person): # THIS METHOD REMOVES/DROPS OFF A PASSENGER FROM THE BUS
        """A METHOD TO ALIGHT A PASSENGER FROM THE BUS"""
        if person in self.passengers: # CHECK IF THE PERSON IS CURRENTLY ON THE BUS
            self.passengers.remove(person) # REMOVE THE PERSON FROM THE LIST OF PASSENGERS (REMOVE METHOD FOR LISTS)
            print(f"{person} has gotten off the bus.") # FRIENDLY MESSAGE TO CONFIRM THE PERSON HAS ALIGHTED
        else:
            print(f"{person} is not on the bus.") # FRIENDLY MESSAGE TO INDICATE THE PERSON WAS NOT FOUND ON THE BUS

    def list_passengers(self): # THIS METHOD LISTS ALL CURRENT PASSENGERS ON THE BUS
        """THIS HELPS US KNOW WHO EXACTLY (PASSENGER NAME) IS ON THE BUS CURRENTLY"""
        if self.passengers: # CHECK IF THERE ARE ANY PASSENGERS ON THE BUS
            print("Current passengers:") # FRIENDLY MESSAGE TO INTRODUCE THE LIST OF PASSENGERS
            for p in self.passengers: # LOOP THROUGH EACH PASSENGER IN THE LIST
                print(f"- {p}") # PRINT EACH PASSENGER'S NAME
        else:
            print("The bus is empty.") # FRIENDLY MESSAGE TO INDICATE THE BUS IS EMPTY

    def status(self): # THIS METHOD SHOWS THE CURRENT STATUS OF THE BUS
        """SHOWS CURRENT STATUS OF THE BUS IN TERMS OF PASSENGERS"""
        current = len(self.passengers)          #HOW MANY PASSENGERS ARE CURRENTLY ON THE BUS
        maximum = self.max_passengers           #WHAT IS THE MAXIMUM CAPACITY OF THE BUS AT THIS POINT
        print(f"Passengers on board: {current}/{maximum}") # PRINTS THE CURRENT NUMBER OF PASSENGERS AGAINST THE MAXIMUM CAPACITY
        
        if current == maximum: # FROM THE ABOVE WE CAN NOW CHECK IF THE BUS IS FULL, EMPTY, OR HAS ROOM (THREE POSSIBILITIES)
            print("The bus is FULL!") #FIRST POSSIBILITY: BUS IS FULL (MESSAGE TO INDICATE THIS)
        elif current == 0:            #SECOND POSSIBILITY: BUS IS EMPTY (MESSAGE TO INDICATE THIS)
            print("The bus is empty.")
        else:                         #THIRD POSSIBILITY: BUS HAS ROOM (MESSAGE TO INDICATE THIS)
            print(f"There is room for {maximum - current} more passengers.")


# =====================================
# NOW WE ARE CREATING THE OBJECTS/INSTANCES OF THE CLASS/FACTORY DEFINED ABOVE
# THIS IS WHERE WE ACTUALLY USE THE CLASS TO CREATE A BUS AND MANAGE PASSENGERS
# =====================================

if __name__ == "__main__": # THIS ENSURES THE CODE BELOW RUNS ONLY WHEN THIS FILE IS EXECUTED DIRECTLY
    # HERE WE ARE CREATING SOME PERSON OBJECTS TO USE AS PASSENGERS
    # THESE PERSONS WILL BE BOARDED AND ALIGHTED FROM THE BUS
    # THIS LIST CAN BE EXPANDED OR MODIFIED AS NEEDED AND WILL WORK ALONGSIDE THE BUS CLASS, MORE PRECISELY THE add_passenger AND remove_passenger METHODS
    # THE EMPTY LIST (self.passengers = []) IN THE BUS CLASS WILL HOLD THESE PERSON OBJECTS
    ana = Person("Ana")
    luis = Person("Luis")
    maria = Person("María")
    carlos = Person("Carlos")
    sofia = Person("Sofía")

    # THIS IS THE ACTUAL BUS OBJECT/INSTANCE CREATION (THIS IS THE LINE WHERE WE USE THE BUS CLASS TO MAKE A BUS OBJECT)
    # WE ARE CREATING A BUS WITH A MAXIMUM CAPACITY OF 4 PASSENGERS (THIS VALUE CAN BE CHANGED AS NEEDED)
    my_bus = Bus(4)

    # WE CAN NOW USE THE METHODS DEFINED IN THE BUS CLASS TO KNOW THE STATUS, BOARD, ALIGHT, AND LIST PASSENGERS
    my_bus.status()

    # HERE WE ARE BOARDING SOME PASSENGERS ON THE BUS
    my_bus.add_passenger(ana)
    my_bus.add_passenger(luis)
    my_bus.add_passenger(maria)
    my_bus.add_passenger(carlos)

    # UP TO THIS POINT, THE BUS SHOULD BE FULL NOW BECAUSE WE'VE SET THE MAXIMUM CAPACITY TO 4
    my_bus.status()

    # HERE WE TRY TO BOARD ANOTHER PASSENGER, WHICH SHOULD FAIL BECAUSE THE BUS IS FULL
    my_bus.add_passenger(sofia)

    # SINCE THE LAST ATTEMPT TO BOARD FAILED, WE WILL NOW TRY TO ALIGHT A PASSENGER TO MAKE ROOM TO BOARD ANOTHER PASSENGER
    my_bus.remove_passenger(luis)
    my_bus.add_passenger(sofia)

    # HERE WE LIST ALL CURRENT PASSENGERS ON THE BUS AND CHECK THE STATUS AGAIN
    my_bus.list_passengers()
    my_bus.status()