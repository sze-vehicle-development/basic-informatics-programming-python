# Simple while loop
expr = True
val = 10.0
while expr:
    print(val)
    # Let's add something to repeat
    val = val + 0.1
    if val > 15:
        expr = False
print(val)
# Backward loop (repeat-while)
val = 15.0
while True:
    print(val)
    val = val - 0.1
    if val <= 10:
        break
# For loop
for i in range(5):
    print(i)
# For loop with a list of ordered elements
for i in [1, 2, 3, 4, 5]:
    print(i)
# For loop with a list of unordered random elements (doubles)
for i in [3.14, 2.71, 1.61, 1.41, 1.0]:
    print(i)