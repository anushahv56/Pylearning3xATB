numbers=[1,2,3,4,5,6,7,8,9]
def doubler(num):
    return num*2
def even_list(num):
    return num%2==0
new_list=list(map(doubler,numbers))
new_even_list=list(filter(even_list,numbers))
print(new_list)
print(new_even_list)
