my_dict={"b": 2,
         "c":3,
         "e":4}
#To find key
for k,v in my_dict.items():
    if k=='b':
        print("B is found")
op='b' in my_dict
print(op)