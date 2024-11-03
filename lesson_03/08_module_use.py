# Using math modules
import math
print(math.cos(0))
print(math.sin(0))
print(math.tan(0))
print(math.exp(1))
print(math.log(2.718281828459045))
print(math.log10(100))
# Using datetime module
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
# Using OS module
import os
print(os.getcwd())
print(os.listdir())
# Using random module
import random
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)
print(random.sample([1, 2, 3, 4, 5], 3))
