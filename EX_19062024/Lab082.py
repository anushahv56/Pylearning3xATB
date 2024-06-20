my_list=[1,2,3,4]
# temp_list=[]
# for i in list:
#     temp=i*2
#     temp_list.append(temp)
# print(temp_list)

def double(num):
    return num*2
#map
#1.takes each element in the list
#2. execute the function on it
#3.return the same number of elements list
double_list=list(map(double(),my_list))
print(double_list)