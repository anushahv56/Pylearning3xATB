# p=lambda a,b:max(a,b)
# print(p(3,4))
# #lambda expression
# def even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(4)
check_even_odd=lambda num:"Even" if num%2==0 else "odd"
print(check_even_odd(4))
