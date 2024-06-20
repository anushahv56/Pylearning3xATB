#tuple--collection of items
#similar to list
#list[] but tuple--()
# list is mutable
#tuple is immutable
my_list =[1,2,3,4]
print(id(my_list))
my_list[2]=20
print(id(my_list))

my_tuple=(1,2,3,4)
print(id(my_tuple))
my_tuple[0]=0
#print(id(my_tuple)) # it doesnot suuport