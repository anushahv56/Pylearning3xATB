#break -->based on condition it iwll kick u out of loop
#pass-- do nothing
for i in range(10):
    if i==5:
        pass   # it will not print 5
    else:
        print(i)
print("outside the loop")