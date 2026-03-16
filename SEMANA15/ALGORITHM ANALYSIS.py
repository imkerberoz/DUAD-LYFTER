"""What is Big O? (SIMPLE EXPLANATION TO REMEMBER)
Big O tells us how slow an algorithm becomes when the input gets bigger.

O(1) = always fast (constant)
O(n) = grows normally (linear)
O(n²) = slow for big lists (quadratic)
O(n X m) or O(n X m X p) = depends on multiple lists

The following is an analogy (as seen in the class) that shows how the lines grow according to the 
Big O notation (which translates to the difficulty of the algorithm represented by the line and the colour of the line. 
Where green is O(1), yellow is O(n), orange is O(n²) and red is O(n X m) or O(n X m X p).

O(1) is a flat line
O(n) is a straight line going up slowly
O(n²) is a curve going up very fast
O(n X m) or O(n X m X p) is a curve going up even faster than O(n²)"""

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------


"""bubble_sort analysis"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#ANSWER: O(n²) - Bubble Sort has two nested loops, each of which can run up to n times, 
# leading to n × n = n² operations in the worst case.

"""IN OTHER WORDS: 
Bubble Sort uses two nested loops.
The outer loop runs n times (n = list size).
The inner loop runs almost n times each time (it decreases slowly).
Total operations: about n × n = n².
Time Complexity: O(n²)
It is slow for large lists because the time grows very fast (quadratic)."""
#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------


"""print_numbers_times_2"""
def print_numbers_times_2(numbers_list):
	for number in numbers_list:
		print(number * 2)
		
#ANSWER: O(n) - This function goes through each number in the list once, so the time it takes grows 
# linearly with the size of the list.

"""IN OTHER WORDS: 
This function has one simple loop.
The loop goes through every number in the list once.
For each number, it does a multiplication and a print (constant time).
If the list has n elements → we do n operations.
Time Complexity: O(n)
It is linear – good speed for normal lists."""

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
"""check_if_lists_have_an_equal"""
def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:
		for element_b in list_b:
			if element_a == element_b:
				return True
				
	return False

#ANSWER: O(n X m) - This function has two nested loops, where the outer loop runs n times (size of list_a) 
#   and the inner loop runs m times (size of list_b).

"""IN OTHER WORDS:
This function uses two nested loops.
Outer loop: goes through list_a (size n).
Inner loop: for each element of list_a, checks every element in list_b (size m).
In the worst case, it compares n X m times.
Time Complexity: O(n X m)
It is slow if both lists are very big."""

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
"""print_10_or_less_elements"""
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)
	for index in range(min(list_len, 10)):
		print(list_to_print[index])
		
#ANSWER: O(1) - This function has a fixed number of operations (up to 10), regardless of the size of the input list.

"""IN OTHER WORDS:
This function prints maximum 10 elements.
It uses min(len(list), 10) → the loop never runs more than 10 times.
Even if the list has 1,000,000 elements, it still does only 10 prints.
Time Complexity: O(1)
Constant time – very fast, does not depend on list size."""

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
"""generate_list_trios"""
def generate_list_trios(list_a, list_b, list_c):
	result_list = []
	for element_a in list_a:
		for element_b in list_b:
			for element_c in list_c:
				result_list.append(f'{element_a} {element_b} {element_c}')
				
	return result_list 

#ANSWER: O(n X m X p) - This function has three nested loops, where the outer loop runs n times (size of list_a),
# the middle loop runs m times (size of list_b), and the innermost loop runs p times (size of list_c).

"""IN OTHER WORDS:
This function has three nested loops.
First loop: list_a (size n)
Second loop: list_b (size m)
Third loop: list_c (size p)
It creates every possible combination → n X m X p elements.
Time Complexity: O(n X m X p)
It grows very fast if the three lists are large (cubic time)."""