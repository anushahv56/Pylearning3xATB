#list-collection of items
my_list=[1,2,3]
#my_list2=[1,2,3,"ABC",True,12.33]
print(my_list[1])
my_list.append(24)  #append add at the end
my_list.extend([12,13]) # add two items at the end
my_list.insert(1,"a") #inser in between the list
print(my_list)
my_list.remove('a') # to remove
print(my_list)
my_copy_list=my_list.copy() #to copy
print(my_copy_list)
my_list.clear() #to clear
print(my_list)
my_copy_list.sort() #to sort in assending order
print(my_copy_list)
my_copy_list.reverse() # to sort in desending order
print(my_copy_list)
