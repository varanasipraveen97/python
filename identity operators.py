# Create three lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Compare lists
print("list1 == list2:", list1 == list2)      # Same content
print("list1 is list2:", list1 is list2)      # Same object?
print("list1 is list3:", list1 is list3)      # Same object?

# Using 'is not'
print("list1 is not list2:", list1 is not list2)
print("list1 is not list3:", list1 is not list3)

# Print memory addresses
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))

#list1 == list2: True
#list1 is list2: False
#list1 is list3: True
#list1 is not list2: True
#list1 is not list3: False
#ID of list1: 2283817529216
#ID of list2: 2283817520192
#ID of list3: 2283817529216
