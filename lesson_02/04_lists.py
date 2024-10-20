# Creation of list
# List is a collection of elements
l = [1, 2, 3, 4, 5]
print(l)
# Arithmetic operations on lists
# Concatenation
print(l + [6, 7, 8, 9, 10])
# Repeat the list 3 times
print(l * 3)
# Slicing
# Get second element
print(l[1])
# Get the first three elements
print(l[:3])
# Get the last two elements
print(l[-2:])
# Get the middle two elements
print(l[1:3])
# Common list operations
# List length
print(len(l))
# Append an element
l.append(6)
print(l)
# Insert an element
l = [1, 2, 3, 4, 5]
l.insert(2, 6)
print(l)
# Remove an element
l = [1, 2, 3, 4, 5]
l.remove(3)
print(l)
# Remove an element by index
l = [1, 2, 3, 4, 5]
l.pop(3)
print(l)
# Reverse list
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)
# Other way
l = [1, 2, 3, 4, 5]
print(l[::-1])
# Sort list
l = [5, 3, 1, 4, 2]
l.sort()
print("Sort: ", l)
# Sort list in reverse order
l = [5, 3, 1, 4, 2]
l.sort(reverse=True)
print("Reverse sort: ", l)
# Aggregation operations
# Sum
l = [1, 2, 3, 4, 5]
print("Sum: ", sum(l))
# Minimum
print("Minimum: ", min(l))
# Maximum
print("Maximum: ", max(l))
# Average
print("Average: ", sum(l) / len(l))
# Create a range
r = range(10)
print("Range: ",r)
print("Range: ",list(r))
for i in r:
    print(i)
# Iterating over a list
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)
# List comprehension
r = range(5)
l2 = [x * 2 for x in r]
print(l2)
# List comprehension with condition
l3 = [x * 2 for x in r if x % 2 == 0]
print(l3)
# Look for an element in a list
l = [1, 2, 3, 4, 5]
print(1 in l)
print(6 in l)
# Look for an element in a list
l = [1, 2, 3, 4, 5]
print(l.index(3))
# Count the number of occurrences of an element
l = [1, 2, 3, 4, 5, 3]
print(l.count(3))
# Clear the list
l = [1, 2, 3, 4, 5]
l.clear()
print(l)