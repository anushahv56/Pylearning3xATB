details={"name":"pramod",
         "age":43,
         "is male":True,
         "Address":"KA"}
print(details.get("Address"))
print(details.values())
print(details.keys())
print(len(details))
print(details["Address"])
my_dic={"a":1,"b":2,"c":23}
print(len(my_dic))
print(my_dic.keys())
print(my_dic.values())
for i in my_dic:
    print(i)
for k,v in my_dic.items():
    print(k,v)