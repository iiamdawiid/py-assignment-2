#Function Exercise 
def full_name(list1, list2):
	name_list = [f"{word} {list2[index]}" for index, word in enumerate(list1)]
	return name_list

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
print(full_name(first_name, last_name))



# Exercise 1 
def lessthan10(num_list):
    final_list = [num for num in num_list if num < 10]
    return final_list

l_1 = [1,11,14,5,8,9]
print(lessthan10(l_1))



# Exercise 2 
def combine_sort(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    return new_list

"""wanted to challenge myself - code tracks frequency of nums in tracker_dict
   and if num occurs more than once it is deleted from new_list"""
def combine_sort2(list1, list2):
    tracker_dict = {}
    new_list = list1 + list2
    new_list.sort()
    
    for num in new_list:
         tracker_dict[num] = tracker_dict.get(num, 0) + 1
    
    for index, num in enumerate(new_list):
        if tracker_dict[num] > 1:
             del new_list[index]
    return new_list

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
print(combine_sort(l_1, l_2))
print(combine_sort2(l_1, l_2))

