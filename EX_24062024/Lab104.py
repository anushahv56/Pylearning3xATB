#Filters in python
#The filter() function in python is built in function
#allows you to filter elements in the list ,tuple,set
numbers=[1,2,3,4,5,6,7,8,9]
#new_list_even=[2,4,6,8]#
def is_even(num):
    return num%2==0
def is_greater(num):
    return num>5

new_list_even=filter(is_even,numbers)
new_list_greater=filter(is_greater,numbers)
print(list(new_list_even))
print(list(new_list_greater))




