# THIS WILL BE AN EXERCISE FILE FOR MULTIPLE INHERITANCE WITH SUPER()
# THIS WILL SHOW A SUBSCRIPTION PLATFORM WITH 3 DIFFERENT TYPE OF USERS: FREE, PREMIUM AND PREMIUM PLUS
# EACH USER TYPE WILL INHERIT FROM A BASE USER CLASS

""" MAIN CLASS FOR USERS (SUPERCLASS) """
class Users: # BASE CLASS FOR ALL USER TYPES
    user_type = "Free" # DEFAULT USER TYPE IS FREE
    adds_allowed = True # FREE USERS WILL HAVE ADS ENABLED
    max_devices = 1 # FREE USERS CAN USE ONLY 1 DEVICE SIMULTANEOUSLY

    def __init__(self, username, name, lastname): # CONSTRUCTOR TO INITIALIZE USER OBJECT
        self.username = username
        self.name = name
        self.lastname = lastname

    def display_info(self): # METHOD TO DISPLAY USER INFORMATION
        print(f"The Username is: {self.username}")
        print(f"The Full Name is: {self.name} {self.lastname}")


""" PREMIUM USER CLASS (SUBCLASS) """
class PremiumUser(Users): # PREMIUM USER CLASS INHERITS FROM USERS
    user_type = "Premium" # OVERRIDE USER TYPE TO PREMIUM
    ads_allowed = False # PREMIUM USERS DO NOT SEE ADS
    max_devices = 3 # PREMIUM USERS CAN USE UP TO 3 DEVICES SIMULTANEOUSLY

    def __init__(self, username, name, lastname, coupon_code, discount): # CONSTRUCTOR TO INITIALIZE PREMIUM USER OBJECT
        self.coupon_code = coupon_code
        self.discount = discount
        self.premium_content_access = True # PREMIUM USERS HAVE ACCESS TO PREMIUM CONTENT
        super().__init__(username, name, lastname) # CALL THE SUPERCLASS CONSTRUCTOR

    def display_info(self): # METHOD TO DISPLAY USER INFORMATION
        super().display_info() # CALL THE SUPERCLASS METHOD TO DISPLAY BASIC INFO FROM USERS CLASS (SUPERCLASS)
        print(f"Your coupon code is: {self.coupon_code}")
        print(f"Your discount is: {self.discount}%")

""" PREMIUM PLUS USER CLASS (SUBCLASS) """

class PremiumPlusUser(PremiumUser): # PREMIUM PLUS USER CLASS INHERITS FROM USERS
    user_type = "Premium Plus" # OVERRIDE USER TYPE TO PREMIUM PLUS
    max_devices = 5 # PREMIUM PLUS USERS CAN USE UP TO 5 DEVICES SIMULTANEOUSLY

    def display_info(self): # METHOD TO DISPLAY USER INFORMATION
        super().display_info() # CALL THE SUPERCLASS METHOD TO DISPLAY BASIC INFO FROM ITS OWN SUPERCLASS (PREMIUM USER)
        print(f"Your premium plus benefits include access to exclusive content and higher device limit of {self.max_devices} devices.")



if __name__ == "__main__": # THIS BLOCK RUNS ONLY WHEN THIS FILE IS EXECUTED DIRECTLY
    # CREATING A FREE USER 
    # THIS IS WHERE THE MAGIC HAPPENS, WE ARE CREATING USERS OUT OF THE CLASSES DEFINED ABOVE
    # FOLLOWING THE ANALOGY OF A USER MANAGEMENT SYSTEM, WE INSTANTIATE DIFFERENT USER TYPES WITH SPECIFIC ATTRIBUTES

    free_user = Users("free_user123", "Alice", "Smith")
    print("Free User Info:")
    free_user.display_info()
    print(f"User Type: {free_user.user_type}, Ads Allowed: {free_user.adds_allowed}, Max Devices: {free_user.max_devices}")
    print()

# CREATING A PREMIUM USER
    premium_user = PremiumUser("premium_user456", "Bob", "Johnson", "SAVE20", 20)
    print("Premium User Info:") 
    premium_user.display_info()
    print(f"User Type: {premium_user.user_type}, Ads Allowed: {premium_user.adds_allowed}, Max Devices: {premium_user.max_devices}")
    print()

#cREATING A PREMIUM PLUS USER
    premium_plus_user = PremiumPlusUser("premium_plus_user789", "Charlie", "Brown", "SAVE30", 30)
    print("Premium Plus User Info:")
    premium_plus_user.display_info()
    print(f"User Type: {premium_plus_user.user_type}, Ads Allowed: {premium_plus_user.adds_allowed}, Max Devices: {premium_plus_user.max_devices}")
    print()