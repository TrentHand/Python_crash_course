#tuples are like lists but they don't ever change in value.  They are permanent values(like a SS#)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#you can't change a tuple's value, but you can reassign the variable to have entirely new values
dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)