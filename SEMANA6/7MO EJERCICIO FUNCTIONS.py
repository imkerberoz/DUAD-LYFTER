def is_prime(n):
    # NUMBERS LESS THAN OR EQUAL TO 1 ARE NOT PRIME
    #NUMBERS LESS THAN 1 OR EQUAL 
    if n <= 1:
        return False
    # CHECK FOR DIVISORS FROM 2 UP TO THE SQUARE ROOT OF N
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: 
            return False
    return True

def get_primes(lst):
    # CREATE AN EMPTY LIST TO STORE PRIME NUMBERS
    primes = []
    # ITERATE THROUGH EACH NUMBER IN THE INPUT LIST
    for num in lst:
        # IF THE NUMBER IS PRIME, ADD IT TO THE PRIMES LIST
        if is_prime(num):
            primes.append(num)
    return primes

# TEST WITH THE GIVEN LIST
lst = [4,55,81,66,44,20,9,7,62,114,55,68,17,3]
result = get_primes(lst)
print(f"The following numbers are Primes:{result}")  