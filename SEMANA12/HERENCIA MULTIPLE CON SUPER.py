#SUBSCRIPTION PLATFORM EXAMPLE - DEMONSTRATING REAL MULTIPLE INHERITANCE USING MIXINS
# INHERITANCE CLASSES ARE GENERALLY USED TO COVER THE "IS-A" RELATIONSHIP, WHILE MIXINS ARE USED TO ADD CAPABILITIES "CAN DO"
# INHERITANCE CHAIN VS MULTIPLE INHERITANCE:
# INHERITANCE CHAIN: A CLASS INHERITS FROM A SINGLE PARENT, WHICH IN TURN INHERITS FROM ANOTHER, FORMING A LINEAR HIERARCHY
# MULTIPLE INHERITANCE: A CLASS INHERITS FROM MULTIPLE INDEPENDENT CLASSES, COMBINING THEIR BEHAVIORS AND ATTRIBUTES
# THIS EXAMPLE SHOWS HOW TO COMBINE MULTIPLE MIXINS TO CREATE COMPLEX USER TYPES
# SCENARIO: A SUBSCRIPTION-BASED PLATFORM WITH DIFFERENT USER TIERS

#INHERITANCE CLASS = USER (BASE CLASS) >> "IS A" - IDENTITY
#MIXINS = NO ADS, MULTI DEVICE, DISCOUNT, EXCLUSIVE ACCESS >> "WHAT CAN DO" - CAPABILITIES

""" Goal: Show how one class can inherit behaviors from MULTIPLE independent classes at once
# Instead of a single chain (linear inheritance), we combine small, focused "mixin" classes """

#IMPORTANT USAGE OF SUPER() IN THE CONSTRUCTORS AND METHODS TO ENSURE PROPER CHAINING
# ALSO IMPORTANT USAGE OF **KWARGS TO ALLOW PASSING ARBITRARY KEYWORD ARGUMENTS THROUGH THE INHERITANCE CHAIN
# ALSO IMPORTANT TO UNDERSTAND THE METHOD RESOLUTION ORDER (MRO) IN MULTIPLE INHERITANCE SCENARIOS
# ALSO IMPORTANT TO MENTION THAT THE ORDER OF INHERITANCE MATTERS FOR THE MRO
# IT IS IMPERATIVE TO UNDERSTAND THAT MIXINS ARE USUALLY SMALL CLASSES THAT ADD A SPECIFIC BEHAVIOR OR ATTRIBUTE
# THEY ARE NOT MEANT TO BE USED STANDALONE, BUT COMBINED WITH OTHER CLASSES TO BUILD COMPLEX BEHAVIORS


# ────────────────────────────────────────────────
""" 
Base class that all users will inherit from.
Contains the common attributes and basic behavior every user shares.
"""
class User:
    user_type = "Free" # CLASS ATTRIBUTE: default type for any user created from this class
    ads_allowed = True # CLASS ATTRIBUTE: free users see ads by default
    max_devices = 1 # CLAsS ATTRIBUTE: maximum simultaneous devices allowed

    def __init__(self, username, name, lastname): # Constructor: initializes the basic user information
        self.username = username       # Unique identifier for login
        self.name = name               # First name
        self.lastname = lastname       # Last name / family name

    def display_info(self): # Method to show basic user details (can be extended by subclasses/mixins)
        print(f"Username: {self.username}")
        print(f"Full Name: {self.name} {self.lastname}")


""" 
Mixin class: Provides "no advertisements" behavior.
Mixins usually don't have __init__ unless they need to set something.
Here we just override the class attribute.
"""
class NoAds:
    ads_allowed = False # Override: ANY CLASS THAT INHERITS THIS MIXIN WILL HAVE ADS DISABLED


""" 
Mixin class: Adds support for multiple devices.
It needs to accept and set max_devices, and it uses **kwargs to cooperate
with other classes in the inheritance chain.
"""
class MultiDevice:
    def __init__(self, max_devices, **kwargs): #HERE WE ARE CREATING THE CONSTRUCTOR AND USING **KWARGS WHICH IS IMPORTANT TO SET FOR MULTIPLE INHERITANCE (NO LIMIT OF PARAMETERS WE CAN PASS / KEYWORD ARGUMENTS)
        self.max_devices = max_devices # SET THE NUMBER OF ALLOWED DEVICES
        super().__init__(**kwargs) # IMPORTANT: CALL super() SO OTHER __init__ METHODS IN THE MRO (METHOD RESOLUTION ORDER) GET CALLED


""" 
Mixin class: Adds coupon code and discount functionality.
Also extends display_info to show discount information.
"""
class Discount:
    def __init__(self, coupon_code=None, discount=0, **kwargs):
        self.coupon_code = coupon_code    # e.g., "SAVE20" or None
        self.discount = discount          # percentage, e.g., 20
        # Call super() to allow other mixins/base classes to initialize
        super().__init__(**kwargs)

    # Override/Extend display_info to include discount details
    def display_info(self): # First call the previous display_info in the MRO chain
        super().display_info()
        if self.coupon_code: # ONLY PRINT IF AN ACTUAL COUPON IS APPLIED
            print(f"Coupon: {self.coupon_code} ({self.discount}% discount)")


""" 
Mixin class: Special benefits only for Premium Plus users.
Mainly adds extra info in display_info.
"""
class ExclusiveAccess:
    # IMPORTANT: NO __init__ NEEDED HERE → WE DON'T HAVE NEW ATTRIBUTES TO SET/ADD
    
    def display_info(self): # Call previous display_info methods first
        super().display_info() # THIS IS IMPORTANT TO MAINTAIN THE CHAIN OF DISPLAY INFO
        print("Premium Plus exclusive: Access to special content + highest device limit") #FRIENDLY MESSAGE FOR THE USER (PREMIUM PLUS USER)


"""UP TO HERE WE HAVE DEFINED THE BASE CLASS AND THE MIXINS 
(A TOTAL OF 4 MIXINS AND 1 BASE CLASS USER WHICH WILL BE COMBINED LATER)"""

# ────────────────────────────────────────────────
# NOW WE CREATE CONCRETE USER TYPES BY COMBINING THE BASE + MULTIPLE MIXINS 
# HERE WE WILL HAVE 3 USER TYPES: FREE, PREMIUM, PREMIUM PLUS

class FreeUser(User):
    """ 
    Free tier user: inherits ONLY from User.
    No extra mixins → keeps default values (ads, 1 device, no discount).
    """
    pass   # NOTHING TO ADD HERE, JUST INHERITS FROM USER


class PremiumUser(User, NoAds, MultiDevice, Discount):
    """ 
    Premium tier: combines SEVERAL mixins at once.
    Order matters for MRO (Method Resolution Order), but super() handles it cooperatively.
    """
    # FIRST THING WE DO IS OVERRIDE THE CLASS ATTRIBUTE USER_TYPE TO "PREMIUM"
    user_type = "Premium"

    def __init__(self, username, name, lastname, coupon_code, discount):
        # PASS ALL NEEDED VALUES TO THE MIXINS/BASE THROUGH SUPER()
        # MAX DEVICES IS SET TO 3 FOR PREMIUM USERS
        # THE FOLLOWING CALL WILL TRIGGER THE CHAIN OF __init__ METHODS IN THE MRO
        # THE ORDER OF PARAMETERS MUST MATCH THE EXPECTATIONS OF EACH MIXIN/BASE CLASS
        # THE **KWARGS IN THE MIXINS ALLOWS US TO PASS EXTRA PARAMETERS WITHOUT ISSUES
        # THE FIRST 3 PARAMETERS ARE INHERITED FROM THE BASE CLASS USER, EXCEPT max_devices, coupon_code, discount
        # THESE LAST 3 PARAMETERS ARE HANDLED BY THE RESPECTIVE MIXINS
        super().__init__(
            username=username,
            name=name,
            lastname=lastname,
            max_devices=3,           #HERE WE OVERRIDE THE MAX DEVICES FOR PREMIUM USERS AND SET IT TO 3 MANUALLY
            coupon_code=coupon_code,
            discount=discount
        )


class PremiumPlusUser(User, NoAds, MultiDevice, Discount, ExclusiveAccess): #ONLY DIFFERENCE IS THE ADDITION OF THE EXCLUSIVE ACCESS MIXIN
    """ 
    Premium Plus: same as Premium, but adds one more mixin (ExclusiveAccess).
    This shows how easy it is to extend by adding more mixins.
    """
    user_type = "Premium Plus" #HERE WE OVERRIDE THE USER TYPE TO "PREMIUM PLUS"

    def __init__(self, username, name, lastname, coupon_code, discount):
        # max_devices=5 IS THE ONLY DIFFERENCE HERE COMPARED TO PREMIUM USER
        # WE CALL SUPER() TO TRIGGER THE CHAIN OF __init__ METHODS IN THE MRO
        # THE ORDER OF PARAMETERS MUST MATCH THE EXPECTATIONS OF EACH MIXIN/BASE CLASS
        # THE **KWARGS IN THE MIXINS ALLOWS US TO PASS EXTRA PARAMETERS WITHOUT ISSUES
        # THE FIRST 3 PARAMETERS ARE INHERITED FROM THE BASE CLASS USER, EXCEPT max_devices, coupon_code, discount
        # THESE LAST 3 PARAMETERS ARE HANDLED BY THE RESPECTIVE MIXINS (WHICH HANDLE THE CAPABILITIES NOT THE USER TYPE)
        super().__init__(
            username=username,
            name=name,
            lastname=lastname,
            max_devices=5,           # SAME LOGIC >> Premium Plus gets 5 devices
            coupon_code=coupon_code,
            discount=discount
        )


# ────────────────────────────────────────────────
# HERE WE TEST THE IMPLEMENTATION
# FOLLOWING THE ANALOGY OF A FACTORY CREATING DIFFERENT USER TYPES
# EACH USER TYPE COMBINES DIFFERENT MIXINS TO PROVIDE SPECIFIC CAPABILITIES
if __name__ == "__main__": # ENTRY POINT FOR TESTING THE CLASSES, THIS ENSURES THE CODE BELOW RUNS ONLY WHEN THIS FILE IS EXECUTED DIRECTLY
    print("=== Free User ===") 
    free = FreeUser("alice_free", "Alice", "Smith")
    free.display_info()
    print(f"Type: {free.user_type} | Ads: {free.ads_allowed} | Devices: {free.max_devices}\n")

    print("=== Premium User ===")
    premium = PremiumUser("bob_prem", "Bob", "Johnson", "SAVE20", 20)
    premium.display_info()
    print(f"Type: {premium.user_type} | Ads: {premium.ads_allowed} | Devices: {premium.max_devices}\n")

    print("=== Premium Plus User ===")
    plus = PremiumPlusUser("charlie_plus", "Charlie", "Brown", "VIP30", 30)
    plus.display_info()
    print(f"Type: {plus.user_type} | Ads: {plus.ads_allowed} | Devices: {plus.max_devices}\n")

# ────────────────────────────────────────────────
    # LAST BUT NOT LEAST: IN COMPARISON TO THE PREVIOUS SIMPLE CODE WHERE I CREATED A INHERITANCE CHAIN AND NOT...
    # A COMPOSED/MULTIPLE INHERITANCE (MRO), THE FOLLOWING PROVES THAT MULTIPLE INHERITANCE IS WORKING (not just a chain)
    print("MRO (Method Resolution Order) for PremiumPlusUser:")
    print(PremiumPlusUser.__mro__)

    print("\nMRO for PremiumUser (to compare):")
    print(PremiumUser.__mro__)