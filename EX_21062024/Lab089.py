#unpacking of tuples
a,b,c=(2,3,4)

t=("E","F","G","H")
#t.append()--not able to use immutable in nature
new_t=list(t)
new_t.append(7)
print(new_t)