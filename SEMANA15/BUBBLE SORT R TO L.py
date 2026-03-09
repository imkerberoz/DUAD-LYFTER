#HERE WE ARE SORTING FROM RIGHT TO LEFT, MEANING WE START COMPARING FROM THE END OF THE LIST TOWARDS THE BEGINNING.
#THE LOGIC IS THE SAME, WE JUST CHANGE THE DIRECTION OF THE INNER LOOP AND THE COMPARISON.

"""
🚀 QUICK REFERENCE - WHAT EACH PART MEANS  

🔢  n = total number of elements in the list (length)
    Example: if list has 7 numbers → n = 7
    -------------------------------------------------------
🔄  i (outer loop) = number of complete passes / rounds
    Also: how many elements are already correctly placed at the beginning
    After i=0 → smallest element is at index 0
    After i=1 → two smallest are in positions 0 and 1, etc.
    --------------------------------------------------------------------------------------------------------------
👈  j (inner loop) = current position we are looking at (FROM RIGHT) (THIS IS LIKE A FINGER POINTING AT THE CURRENT PAIR THAT WE ARE CHECKING)
    We compare arr[j] with arr[j-1]  (this element ◀️ previous element)
    -------------------------------------------------------
◀️ j-1 = the neighbor to the left of j
    We always compare two adjacent (next to each other) elements
    -------------------------------------------------------
🔀  swap (AKA: MAGIC SWAP) = exchange / interchange two values when they are in wrong order
    In Python: arr[j], arr[j-1] = arr[j-1], arr[j]
    -------------------------------------------------------
🎯  Goal       = after all passes, the list is sorted from smallest → largest
    -------------------------------------------------------
"""

"""
SMALL NOTE - THE MAGIC SWAP LINE (right-to-left version):
arr[j], arr[j - 1] = arr[j - 1], arr[j]  NOTE:in maths anything that runs to the left is smaller, so we compare arr[j] < arr[j-1]


→ Swaps the current element with its left neighbor
→ This swaps two values in ONE line without losing data.
→ It's the same as:   a, b = b, a
→ Python does it simultaneously → no need for a temporary variable.
→ Reason we can't do it in two lines: 
    arr[j] = arr[j-1]; arr[j-1] = arr[j] → would copy the same value twice and lose the original.
"""


def bubble_sort(arr):  # 🔧 FUNCTION THAT TAKES A LIST OF NUMBERS (ARRAY)
    n = len(arr)                        # 🔢 Get how many items we have  (N IS COMPOSED OF HOW MANY ITEMS WE'VE GOT ON THE LIST)
    
    for i in range(n):                  # 🔄 Each full pass / round
        for j in range(n - 1, i, -1):   # 👈 Walk through the list comparing pairs (FROM RIGHT TO LEFT )
            if arr[j] < arr[j - 1]:     # Compare this one ◀️ with the previous one (FROM RIGHT TO LEFT ◀️)
                arr[j], arr[j - 1] = arr[j - 1], arr[j]   # 🔀 Swap if wrong order (ANOTER WAY TO PUT IT IS: a, b = b, a)
        
    return arr                          # 🎯 Return the now-sorted list


# ────────────────────────────────────────────────
#                  EXAMPLE USAGE
# ────────────────────────────────────────────────

# Example 1: Numbers
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", numbers)
bubble_sort(numbers)
print("After sorting (right to left) :", numbers)
# Expected: [11, 12, 22, 25, 34, 64, 90]

# Example 2: Already sorted list
already_sorted = [1, 3, 5, 7, 9]
print("\nBefore sorting:", already_sorted)
bubble_sort(already_sorted)
print("After sorting (right to left):", already_sorted)
# Remains: [1, 3, 5, 7, 9]

# Example 3: Letters / strings
letters = ['k', 'b', 'm', 'a', 'z', 'p']
print("\nBefore sorting:", letters)
bubble_sort(letters)
print("After sorting (right to left) :", letters)
# Expected: ['a', 'b', 'k', 'm', 'p', 'z']

# Example 4: With negative numbers and duplicates
mixed = [5, -3, 8, 0, -3, 12, 5]
print("\nBefore sorting:", mixed)
bubble_sort(mixed)
print("After sorting (right to left) :", mixed)
# Expected: [-3, -3, 0, 5, 5, 8, 12]

# IMPORTANT NOTE: 
""" WHY THE SAME CODE WORKS FOR NUMBERS AND LETTERS:

Python's comparison operators (>, <, ==) work on many types:
- For numbers: compares their actual mathematical value (5 < 10 → True)
- For strings/letters: compares their "ordinal" value (Unicode/ASCII code)
    - 'a' has code 97
    - 'b' has code 98
    - so 'a' < 'b' is True (97 < 98)
    - Uppercase comes before lowercase: 'A' (65) < 'a' (97)

When bubble sort does: if arr[j] > arr[j + 1]
→ Python automatically knows what "greater" means for the type inside the list

As long as all elements are comparable (all numbers OR all strings),
the algorithm works exactly the same way — no changes needed!

Examples:
- [64, 34, 25, 12] → compares numbers
- ['k', 'b', 'm', 'a'] → compares letter codes → 'a' < 'b' < 'k' < 'm'
- ['apple', 'banana', 'cherry'] → compares strings letter-by-letter

Magic: Bubble sort doesn't care about the type — Python handles the comparison! """
