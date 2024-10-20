# Create a set
s = {1, 2, 3, 4, 5}
print(s)
# Add an element
s.add(6)
print(s)
# Remove an element
s = {1, 2, 3, 4, 5}
s.remove(3)
print(s)
# Set operations
# Union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2))
# Alternative
print(s1 | s2)
# Intersection
print(s1.intersection(s2))
# Alternative
print(s1 & s2)
# Difference
print(s1.difference(s2))
# Alternative
print(s1 - s2)
# Symmetric difference
print(s1.symmetric_difference(s2))
# Alternative
print(s1 ^ s2)
# Subset
print(s1.issubset(s2))
# Superset
print(s1.issuperset(s2))
# Disjoint
print(s1.isdisjoint(s2))
# Containment
print(1 in s1)
print (6 in s1)
#