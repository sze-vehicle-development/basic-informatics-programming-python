# Create dictionary
d = {"a": 1, "b": 2, "c": 3}
print(d)
# Access elements
print(d["a"])
print(d["b"])
print(d["c"])
# Add element
d["d"] = 4
print(d)
# Remove element
del d["a"]
print(d)
# Dictionary operations
d = {"a": 1, "b": 2, "c": 3}
# Dictionary length
print(len(d))
# Dictionary keys
print(d.keys())
# Dictionary values
print(d.values())
# Dictionary items
print(d.items())
# Iterating over a dictionary
for k in d:
    print(k, d[k])
# Dictionary comprehension
d = {k: v for k, v in zip("abc", range(3))}
print(d)
# Dictionary comprehension with condition
d = {k: v for k, v in zip("abc", range(3)) if v % 2 == 0}
print(d)

