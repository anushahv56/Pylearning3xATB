numbers=[1,2,3,4,5,6,7]
def double_me(num):
    return num*2
new_list=map(double_me,numbers)
print(list(new_list))

def even_num(num):
    return num%2==0
new=filter(even_num,numbers)
print(list(new))