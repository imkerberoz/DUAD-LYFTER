#Define my list
my_list1 = [6, 3, 6, 5, 10]    
my_list2 = ["Dog", "Cat", "Mouse", "Bird", "Fish"]

#Check if the list has at least 2 elements to swap
if len(my_list1) < 2:
    print("The list is too short to swap elements.")    
else:
    #Swap the first and last element using multiple assignment
    my_list1[0], my_list1[-1] = my_list1[-1], my_list1[0]
    my_list2[0], my_list2[-1] = my_list2[-1], my_list2[0]
    
    #Print the resulting list
    print(my_list1)
    print(my_list2)

