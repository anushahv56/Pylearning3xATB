#Function-- if we want to reuse the code we can use function
#print,input(),type(),format,min(),max(),sum(),len(),avg()

#string
name="Amit"
print(type(name))
print(id(name))  # it gives address/memory location of the variable
print(len(name))  # it gives length of the string--4
print(name.upper())
print(name.lower())
a=name.count('a')
print(a)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
#print(name[4])  #string index out of range
#String is immutable in ature
name[0]="s"
print(name)